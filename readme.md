<h1>Conexão entre Docker e DBeaver</h1>

<p>Para conectar com o docker e o DBeaver precisamos rodar as duas imagens, sendo uma para aplicação das rotas e a outra para o banco de dados myslq</p>

<p>Comando para rodar a imagem das rotas: docker run -p 3000:5000 --network mynet docker-pythonv3</p>
<p>Comando para rodar a imagem do bando de dados:docker run -e MYSQL_ROOT_PASSWORD=lhama --name mysqldb --network mynet -p 3306:3306 -v mysqlVolume:/var/lib/mysql -d mysql:latest</p>

<h2>Conexão com o DBeaver</h2>
<p>Ao conectar com o DBeaver será necessário criar uma conexão colocando o host como 0.0.0.0</p>