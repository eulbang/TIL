-- restaurants 테이블의 이름을 restaurant_info로 변경
ALTER TABLE restaurants
RENAME TO restaurant_info;

-- menus 테이블의 이름을 menu_items로 변경
ALTER TABLE menus
RENAME TO menu_items;

-- restaurant_info 테이블에서 location 컬럼의 이름을 address 변경
ALTER TABLE restaurant_info
RENAME COLUMN location TO address;

-- menu_items 테이블에 available 컬럼 추가하고, 기본값을 TRUE로 설정
ALTER TABLE menu_items
ADD COLUMN available BOOLEAN DEFAULT TRUE;

-- reviews 테이블 삭제
DROP TABLE menu_items;