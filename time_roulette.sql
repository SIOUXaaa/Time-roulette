DROP TABLE IF EXISTS remind;
DROP TABLE IF EXISTS memo;
DROP TABLE IF EXISTS schedule;
DROP TABLE IF EXISTS user;

CREATE TABLE user
(
    id   int(11) primary key NOT NULL AUTO_INCREMENT,
    name varchar(255) UNIQUE NULL DEFAULT NULL,
    password varchar(255)        NULL DEFAULT NULL,
    avatar varchar(255) NULL DEFAULT 'avatar/',
    time timestamp(0)        NULL DEFAULT CURRENT_TIMESTAMP(0)
);

CREATE TABLE schedule
(
    schedule_id int(11) primary key AUTO_INCREMENT,
    user_id     int(11)             NOT NULL,
    title       varchar(1024)       NULL DEFAULT NULL,
    contents    TEXT                NULL DEFAULT NULL,
    address     varchar(255)        NULL DEFAULT NULL,
    time        timestamp(0)        NULL DEFAULT '2000-1-1 0:0:0',
    FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE memo
(
    memo_id  int(11) PRIMARY KEY AUTO_INCREMENT,
    user_id  int(11)      NOT NULL,
    contents text         NULL     DEFAULT NULL,
    done     bool         NOT NULL DEFAULT false,
    reminded bool         NOT NULL DEFAULT true,
    time     timestamp(0) NULL     DEFAULT '2000-1-1 0:0:0',
    FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE remind
(
    remind_id int(11) PRIMARY KEY AUTO_INCREMENT,
    user_id   int(11)                   NOT NULL,
    type      enum ('schedule', 'memo') NOT NULL,
    type_id   int(11)                   NOT NULL,
    time      timestamp(0)              NULL DEFAULT '2000-1-1 0:0:0',
    FOREIGN KEY (user_id) REFERENCES user (id),
    FOREIGN KEY (type_id) REFERENCES schedule (schedule_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES memo (memo_id) ON DELETE CASCADE
);

CREATE TRIGGER add_user
    BEFORE INSERT
    ON user
    FOR EACH ROW
BEGIN
    SET NEW.id = (SELECT Max(id) + 1 FROM user);
END;

CREATE TRIGGER update_time
    BEFORE INSERT
    ON user
    FOR EACH ROW SET NEW.time = CURRENT_TIMESTAMP(0);


CREATE TRIGGER add_schedule
    BEFORE INSERT
    ON schedule
    FOR EACH ROW
BEGIN
    SET NEW.schedule_id = (SELECT Max(schedule_id) + 1 FROM schedule);
END;

CREATE TRIGGER add_memo
    BEFORE INSERT
    ON memo
    FOR EACH ROW
BEGIN
    SET NEW.memo_id = (SELECT COUNT(*) + 1 FROM memo);
END;

CREATE TRIGGER add_remind
    BEFORE INSERT
    ON remind
    FOR EACH ROW
BEGIN
    SET NEW.remind_id = (SELECT COUNT(*) + 1 FROM remind);
END;

INSERT INTO user(id, name, password)
VALUES (1, 'test01', '123456'),
       (2, 'test02', '123456');

INSERT INTO schedule(user_id, title, contents, address, time)
VALUES (1, '吃饭', '今天要吃饭', '南区大饭店', '2023-5-23 20:54:00'),
       (2, '吃饭', '今天要吃饭', '南区大饭店', '2023-5-23 20:54:00'),
       (1, '吃饭', '今天要吃饭', '南区大饭店', '2023-5-23 20:54:00');

INSERT INTO memo
VALUES (1, 1, '今天要吃饭', false, true, '2023-5-23 20:54:00'),
       (2, 2, '今天要吃饭', false, true, '2023-5-23 20:54:00'),
       (3, 1, '今天要吃饭', false, true, '2023-5-23 20:54:00');

INSERT INTO remind(user_id, type, type_id, time)
VALUES (1, 'schedule', 1, '2023-5-23 20:54:00'),
       (2, 'memo', 2, '2023-5-23 20:54:00');