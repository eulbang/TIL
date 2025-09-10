-- 제1정규형(1NF)
-- 모든 속성이 원자값을 가져야 하므로, 중복된 데이터가 없어야 한다.
-- 사용자 테이블을 분리하여 원자값을 가지도록 한다.

CREATE TABLE Users (
    사용자ID INT PRIMARY KEY,
    이름 VARCHAR(50),
    이메일 VARCHAR(100)
);

CREATE TABLE Posts (
    게시물ID INT PRIMARY KEY,
    사용자ID INT,
    게시물제목 VARCHAR(100),
    게시물내용 TEXT,
    FOREIGN KEY (사용자ID) REFERENCES Users(사용자ID)
);

CREATE TABLE Comments (
    댓글ID INT PRIMARY KEY,
    게시물ID INT,
    댓글내용 TEXT,
    FOREIGN KEY (게시물ID) REFERENCES Posts(게시물ID)
);
전화번호 | 나이 | 플랫폼 |

lee@google.com
-- 제2정규형(2NF)
-- 제1정규형을 만족하고, 기본 키가 아닌 모든 속성이 기본 키에 완전 함수적 종속이어야 한다.
-- 이미 제1정규형에서 분리하여 완전 함수적 종속성을 만족한다.

-- 제3정규형(3NF)
-- 제2정규형을 만족하고, 기본 키가 아닌 모든 속성이 기본 키에 이행적 함수적 종속이 없어야 한다.
-- 이미 제2정규형에서 이행적 함수적 종속성을 제거하여 만족한다.