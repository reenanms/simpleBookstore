CREATE DATABASE livrariaVirtual;

USE livrariaVirtual;

-- Cadastro de clientes:
CREATE TABLE cliente
(
	id INT NOT NULL AUTO_INCREMENT,
	cpf VARCHAR(15) NOT NULL,
	nome VARCHAR(255) NOT NULL,
	PRIMARY KEY (id)
);

-- Cadastro de livros:
CREATE TABLE livro
(
   id INT NOT NULL AUTO_INCREMENT,
	isbn VARCHAR(20) NOT NULL,
	titulo VARCHAR(255) NOT NULL,
	autor VARCHAR(255) NOT NULL,
	anoPublicacao YEAR NOT NULL,
	quantidadeEstoque INT NOT NULL,
	preco FLOAT NOT NULL,
	ativo BIT NOT NULL,
	PRIMARY KEY (id)
);

-- Cadastro de pedidos
CREATE TABLE pedido
(
	id INT NOT NULL AUTO_INCREMENT,
	idCliente INT NULL,
	dataPedido DATETIME NOT NULL,
	confirmacaoPagamento BOOL NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (idCliente) REFERENCES cliente (id)
);

-- Cadastro de livros do pedido
CREATE TABLE pedidoLivro
(
   idPedido INT NOT NULL,
   idLivro INT NOT NULL,
   quantidade INT NOT NULL,
   preco FLOAT NOT NULL,
	PRIMARY KEY (idPedido, idLivro),
	FOREIGN KEY (idPedido) REFERENCES pedido (id),
	FOREIGN KEY (idLivro) REFERENCES livro (id)
);

	
	
-- TRIGGERS: de verificação e atualização de estoque
DELIMITER /validaDescontaEstoque/
	CREATE TRIGGER validaDescontaEstoque BEFORE INSERT
		ON pedidoLivro FOR EACH ROW
	BEGIN
		SET @quantidadeEstoque = (SELECT l.quantidadeEstoque FROM livro l WHERE l.id = NEW.idLivro);			
		SET @quantidadeCompra = NEW.quantidade;
		SET @novaQuanttidade = @quantidadeEstoque - @quantidadeCompra;
														
		IF (@novaQuanttidade < 0) THEN
				SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Livro sem o estoque necessário para efetivar a venda';
		END IF;
	END; /validaDescontaEstoque/
DELIMITER ;

DELIMITER /descontaEstoque/
	CREATE TRIGGER descontaEstoque AFTER INSERT
		ON pedidoLivro FOR EACH ROW
	BEGIN
		SET @quantidadeEstoque = (SELECT l.quantidadeEstoque FROM livro l WHERE l.id = NEW.idLivro);			
		SET @quantidadeCompra = NEW.quantidade;
		SET @novaQuanttidade = @quantidadeEstoque - @quantidadeCompra;
		
		UPDATE livro
		SET quantidadeEstoque = @novaQuanttidade
		WHERE l.id = NEW.idLivro;

	END; /descontaEstoque/
DELIMITER ;

DELIMITER /validaUpdateEstoque/
	CREATE TRIGGER validaUpdateEstoque BEFORE UPDATE
		ON pedidoLivro FOR EACH ROW
	BEGIN
		IF (OLD.idLivro <> NEW.idLivro) THEN
				SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'O livro não pode ser alterado, remova e insira novamente o registro';
		END IF;

		SET @quantidadeEstoque = (SELECT l.quantidadeEstoque FROM livro l WHERE l.id = NEW.idLivro);			
		SET @quantidadeCompra = (NEW.quantidade - OLD.quantidade);
		SET @novaQuanttidade = @quantidadeEstoque - @quantidadeCompra;
												
		IF (@novaQuanttidade < 0) THEN
				SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Livro sem o estoque necessário para efetivar a venda';
		END IF;
	END; /validaUpdateEstoque/
DELIMITER ;

DELIMITER /updateEstoque/
	CREATE TRIGGER updateEstoque AFTER UPDATE
		ON pedidoLivro FOR EACH ROW
	BEGIN
		SET @quantidadeEstoque = (SELECT l.quantidadeEstoque FROM livro l WHERE l.id = NEW.idLivro);			
		SET @quantidadeCompra = (NEW.quantidade - OLD.quantidade);
		SET @novaQuanttidade = @quantidadeEstoque - @quantidadeCompra;
														
		UPDATE livro
		SET quantidadeEstoque = @novaQuanttidade
		WHERE l.id = NEW.idLivro;
	END; /updateEstoque/
DELIMITER ;

DELIMITER /incrementaEstoque/
	CREATE TRIGGER incrementaEstoque AFTER DELETE
		ON pedidoLivro FOR EACH ROW
	BEGIN
		SET @quantidadeEstoque = (SELECT l.quantidadeEstoque FROM livro l WHERE l.id = OLD.idLivro);			
		SET @quantidadeCompra = OLD.quantidade;
		SET @novaQuanttidade = @quantidadeEstoque + @quantidadeCompra;
		
		UPDATE livro
		SET quantidadeEstoque = @novaQuanttidade
		WHERE l.id = OLD.idLivro;

	END; /incrementaEstoque/
DELIMITER ;



INSERT INTO livro (isbn,titulo, autor, anoPublicacao, quantidadeEstoque, preco, ativo)
VALUES
('7894561233654','João e o pé de feijão', 'João João', 2010, 5, 25.90, 1),
('7894563215548', 'Margarida e a flor', 'Pedro Paulo', 2009, 2, 35.90, 1),
('7894563215510', 'Harry Potter e a pedra filosofal', 'J.K. Rowling ', 2017, 5, 10.90, 1),
('7894563215511', 'Harry Potter e a Câmara Secreta', 'J.K. Rowling ', 2017, 5, 15.90, 1),
('7894563215512', 'Harry Potter e o prisioneiro de Azkaban', 'J.K. Rowling ', 2017, 2, 20.90, 1);

