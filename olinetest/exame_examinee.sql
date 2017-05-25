DROP TABLE IF EXISTS [exame_examinee];
CREATE TABLE [exame_examinee]([rowid] INTEGER, [userid] varchar(30), [username] varchar(30), [ticketnumber] varchar(30), [idcard] varchar(18), [password] varchar(1000), [actstatus] varchar(32), [phone] varchar(11), [email] varchar(32), [address] varchar(100), [sex] varchar(4));

INSERT INTO [exame_examinee]([rowid], [userid], [username], [ticketnumber], [idcard], [password], [actstatus], [phone], [email], [address], [sex])
VALUES(1, '56f2d975c57469433dff08bb', '管理员', '1458755909990', '', '1234560', '999999', '18314462409', '1483767097@qq.com', '云南丽江', '1');

INSERT INTO [exame_examinee]([rowid], [userid], [username], [ticketnumber], [idcard], [password], [actstatus], [phone], [email], [address], [sex])
VALUES(2, '56f2db42c57469433dff08bc', '化缘', '1459049619668', '', '1234560', '1', '18314462400', '1483767097@qq.com', '云南丽江', '1');

INSERT INTO [exame_examinee]([rowid], [userid], [username], [ticketnumber], [idcard], [password], [actstatus], [phone], [email], [address], [sex])
VALUES(3, '20170418165514', 'dsvds', '1492505688931', '533221199311281314', '281314', '1', '18314462408', '1@qq.com', 'sagfvd', '0');

INSERT INTO [exame_examinee]([rowid], [userid], [username], [ticketnumber], [idcard], [password], [actstatus], [phone], [email], [address], [sex])
VALUES(4, '20170421111223', '和相鹏', '1492744292044', '533221199311281314', '281314', '1', '18314462401', '18314462401@qq.com', 'asfsdf', '1');

INSERT INTO [exame_examinee]([rowid], [userid], [username], [ticketnumber], [idcard], [password], [actstatus], [phone], [email], [address], [sex])
VALUES(5, '20170421111728', '手感好', '1492744605907', '533221199311281314', '281314', '1', '18314462403', 'sd@qq.com', '扫地机', '1');

