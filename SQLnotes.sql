#MySQL

CREATE TABLE user_id (
	User_id VarChar(20) PRIMARY KEY, );

CREATE TABLE LookUp_Corp(
	Corp_name VarChar(15),
	Start_funding int,);

CREATE TABLE char_id (
	User_id VarChar(20) FOREIGN KEY (user_id(User_id)),
	char_id VarChar(20) PRIMARY KEY,
	rank int,
	Profession VarChar(20),
	Division VarChar(20),
	level int)
CREATE TABLE char_HP(
	char_id VarChar(20) FOREIGN KEY	(user_id(User_id))
	hp_total int,
	hp_curr int,
	mashing varChar (40));
