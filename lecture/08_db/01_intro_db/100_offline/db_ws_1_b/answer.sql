-- restaurants 테이블에 phone_number 필드 추가
ALTER TABLE restaurants
ADD COLUMN phone_number VARCHAR(20);

-- menus 테이블에 description 필드 추가
ALTER TABLE menus
ADD COLUMN description TEXT;

-- restaurants 테이블에서 name 컬럼의 이름을 restaurant_name으로 수정
ALTER TABLE restaurants
RENAME COLUMN name TO restaurant_name;

-- menus 테이블에서 price 컬럼의 자료형을 DECIMAL(12, 2)로 변경하고, NULL을 허용하지 않도록 수정
ALTER TABLE menus
MODIFY COLUMN price DECIMAL(12, 2) NOT NULL;
