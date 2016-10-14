-- Table: menuplan

-- DROP TABLE menuplan;

CREATE TABLE menuplan
(
  id serial NOT NULL,
  date_info date,
  starter text,
  main text,
  dessert text,
  creation_dt timestamp without time zone,
  CONSTRAINT un_date UNIQUE (date_info)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE menuplan
  OWNER TO weingrill;
