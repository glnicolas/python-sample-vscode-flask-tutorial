  <?php

echo "Hello World!";

$host = '192.168.240.176';
$db   = 'pythonlogin';
$user = 'admindb';
$pass = 'CCADt3st1#';
$port = "3306";
$charset = 'utf8mb4';

$options = [
    \PDO::ATTR_ERRMODE            => \PDO::ERRMODE_EXCEPTION,
    \PDO::ATTR_DEFAULT_FETCH_MODE => \PDO::FETCH_ASSOC,
    \PDO::ATTR_EMULATE_PREPARES   => false,
];
$dsn = "mysql:host=$host;dbname=$db;charset=$charset;port=$port";
try {
     $pdo = new \PDO($dsn, $user, $pass, $options);
     echo "ok";
} catch (\PDOException $e) {
     throw new \PDOException($e->getMessage(), (int)$e->getCode());
}