# Microservice

## 一、开发环境搭建

### 1. Python 安装配置

```bash
# 1. 创建虚拟环境
python3 -m venv venv

# 2. 激活虚拟环境
source venv/bin/activate

# 3. 安装依赖包
pip install -r requirements.txt -i https://pypi.douban.com/simple
```

### 2. MySQL 数据库创建

```sql
# 使用 root 账户，创建数据库 RobotDetection, 数据库中执行下面命令创建数据库用户
CREATE DATABASE IF NOT EXISTS Microservice
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;

CREATE DATABASE IF NOT EXISTS Statistics
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;

use mysql
CREATE USER 'AntMan'@'%'IDENTIFIED BY 'ScottLang@181';
GRANT ALL ON Microservice.* TO 'AntMan'@'%';
GRANT ALL ON Statistics.* TO 'AntMan'@'%';
FLUSH PRIVILEGES;
```
