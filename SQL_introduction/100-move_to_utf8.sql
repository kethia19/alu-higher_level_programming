USE hbtn_0c_0;  -- Select the database

-- Change the database character set and collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Change the table character set and collation
ALTER TABLE first_table DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Ensure the 'name' column uses the correct collation without explicitly setting CHARACTER SET
ALTER TABLE first_table CHANGE name name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
