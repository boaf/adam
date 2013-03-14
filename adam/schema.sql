drop table if exists skills;
create table skills (
  id integer primary key,
  name string(150) not null,
  groupId integer references skill_groups (id)
);

drop table if exists skill_groups;
create table skill_groups (
  id integer primary key,
  name string(150) not null
);