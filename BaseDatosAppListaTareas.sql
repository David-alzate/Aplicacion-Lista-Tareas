--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4
-- Dumped by pg_dump version 15.4

-- Started on 2024-07-09 18:29:22

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16427)
-- Name: tareas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tareas (
    id integer NOT NULL,
    titulo text NOT NULL,
    descripcion text NOT NULL,
    estado boolean
);


ALTER TABLE public.tareas OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16426)
-- Name: tareas_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tareas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tareas_id_seq OWNER TO postgres;

--
-- TOC entry 3331 (class 0 OID 0)
-- Dependencies: 214
-- Name: tareas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tareas_id_seq OWNED BY public.tareas.id;


--
-- TOC entry 217 (class 1259 OID 16443)
-- Name: tareasrealizadas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tareasrealizadas (
    id integer NOT NULL,
    titulo character varying(255),
    descripcion text,
    estado boolean
);


ALTER TABLE public.tareasrealizadas OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16442)
-- Name: tareasrealizadas_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tareasrealizadas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tareasrealizadas_id_seq OWNER TO postgres;

--
-- TOC entry 3332 (class 0 OID 0)
-- Dependencies: 216
-- Name: tareasrealizadas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tareasrealizadas_id_seq OWNED BY public.tareasrealizadas.id;


--
-- TOC entry 3178 (class 2604 OID 16430)
-- Name: tareas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tareas ALTER COLUMN id SET DEFAULT nextval('public.tareas_id_seq'::regclass);


--
-- TOC entry 3179 (class 2604 OID 16446)
-- Name: tareasrealizadas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tareasrealizadas ALTER COLUMN id SET DEFAULT nextval('public.tareasrealizadas_id_seq'::regclass);


--
-- TOC entry 3181 (class 2606 OID 16434)
-- Name: tareas tareas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tareas
    ADD CONSTRAINT tareas_pkey PRIMARY KEY (id);


--
-- TOC entry 3183 (class 2606 OID 16450)
-- Name: tareasrealizadas tareasrealizadas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tareasrealizadas
    ADD CONSTRAINT tareasrealizadas_pkey PRIMARY KEY (id);


-- Completed on 2024-07-09 18:29:23

--
-- PostgreSQL database dump complete
--

