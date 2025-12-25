#include <iostream>
#include <memory>

// Интерфейс
class Database {
public:
    virtual void save(const std::string& data) = 0;
    virtual ~Database() = default;
};

// Реализация
class PostgreSQL : public Database {
public:
    void save(const std::string& data) override {
        std::cout << "Saving '" << data << "' to PostgreSQL" << std::endl;
    }
};

// Класс с внедрением зависимости
class Service {
public:
    Service(std::shared_ptr<Database> db) : database(db) {}

    void processData(const std::string& data) {
        database->save(data);
    }

private:
    std::shared_ptr<Database> database;
};

int main() {
    auto db = std::make_shared<PostgreSQL>();
    Service service(db);
    service.processData("Hello, DI in C++!");

    return 0;
}
