-- Table: subscriber

-- DROP TABLE subscriber;

CREATE TABLE subscriber
(
  id serial NOT NULL,
  email text,
  creation_dt timestamp without time zone,
  active boolean
)
WITH (
  OIDS=FALSE
);
ALTER TABLE subscriber
  OWNER TO weingrill;
