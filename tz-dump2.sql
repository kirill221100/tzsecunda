
truncate TABLE organizations CASCADE;
TRUNCATE TABLE organization_activity;
TRUNCATE TABLE buildings CASCADE;
TRUNCATE TABLE activities CASCADE;

INSERT INTO public.activities VALUES ('dcde24f5-45db-4b88-bed2-5174f95ba9f7', 'Еда', NULL);
INSERT INTO public.activities VALUES ('dd8e48b6-846a-4ca1-8199-15bd0ab0b797', 'Мясная продукция', 'dcde24f5-45db-4b88-bed2-5174f95ba9f7');
INSERT INTO public.activities VALUES ('dfeb732d-b573-404c-a57c-88903b8e2ddf', 'Молочная продукция', 'dcde24f5-45db-4b88-bed2-5174f95ba9f7');
INSERT INTO public.activities VALUES ('b538be78-43b5-43dd-b6b9-817dd660a6db', 'Колбасы', 'dd8e48b6-846a-4ca1-8199-15bd0ab0b797');
INSERT INTO public.activities VALUES ('f86aac8d-6633-4cd8-b770-e3ca85441ee1', 'Копчености', 'dd8e48b6-846a-4ca1-8199-15bd0ab0b797');
INSERT INTO public.activities VALUES ('d8423087-ec53-41be-993a-dccb311003b6', 'Молоко', 'dfeb732d-b573-404c-a57c-88903b8e2ddf');
INSERT INTO public.activities VALUES ('b1585d0c-e64c-4ad3-8e6b-cb1f556b1a18', 'Сыры', 'dfeb732d-b573-404c-a57c-88903b8e2ddf');
INSERT INTO public.activities VALUES ('15cc868d-a43c-40d7-897d-c1873502699b', 'Автомобили', NULL);
INSERT INTO public.activities VALUES ('eadcc3a4-8c20-433d-b88c-1e6bce2202b4', 'Грузовые', '15cc868d-a43c-40d7-897d-c1873502699b');
INSERT INTO public.activities VALUES ('6d16545f-04e9-43be-87ec-bc9c9a7c8347', 'Легковые', '15cc868d-a43c-40d7-897d-c1873502699b');
INSERT INTO public.activities VALUES ('7ab9e0a2-f3d3-4352-80b4-9cd844fc6162', 'Запчасти', '6d16545f-04e9-43be-87ec-bc9c9a7c8347');


--
-- TOC entry 3452 (class 0 OID 123085)
-- Dependencies: 216
-- Data for Name: buildings; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.buildings VALUES ('e24c98ef-4ac8-453c-81f1-1d27545c8a78', 'Красная пл., 3, ГУМ, Москва, 109012', 55.75497, 37.62026);
INSERT INTO public.buildings VALUES ('56fb6d1f-659d-4883-9f3b-7cd3fbf5bb58', 'г. Москва, ул. Ленина 1, офис 3', 55.75582, 37.61763);
INSERT INTO public.buildings VALUES ('69dfeb1f-e72d-44a2-893c-db8c1e66ccd7', 'Блюхера, 32/1', 55.83345, 37.56731);


--
-- TOC entry 3454 (class 0 OID 123104)
-- Dependencies: 218
-- Data for Name: organization_activity; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.organization_activity VALUES ('67af8e6d-20b4-4fe0-b921-058578bf68dd', 'dd8e48b6-846a-4ca1-8199-15bd0ab0b797');
INSERT INTO public.organization_activity VALUES ('67af8e6d-20b4-4fe0-b921-058578bf68dd', 'dfeb732d-b573-404c-a57c-88903b8e2ddf');
INSERT INTO public.organization_activity VALUES ('5e3c030c-d02c-43fa-b097-d162f80fb944', 'eadcc3a4-8c20-433d-b88c-1e6bce2202b4');
INSERT INTO public.organization_activity VALUES ('5e3c030c-d02c-43fa-b097-d162f80fb944', '7ab9e0a2-f3d3-4352-80b4-9cd844fc6162');
INSERT INTO public.organization_activity VALUES ('9dd19a62-2235-4e8c-8bd4-9706b968a405', 'd8423087-ec53-41be-993a-dccb311003b6');
INSERT INTO public.organization_activity VALUES ('9dd19a62-2235-4e8c-8bd4-9706b968a405', 'b1585d0c-e64c-4ad3-8e6b-cb1f556b1a18');


--
-- TOC entry 3453 (class 0 OID 123092)
-- Dependencies: 217
-- Data for Name: organizations; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.organizations VALUES ('9dd19a62-2235-4e8c-8bd4-9706b968a405', 'ооо вкусно и точка', '{8-800-555-35-35}', 'e24c98ef-4ac8-453c-81f1-1d27545c8a78');
INSERT INTO public.organizations VALUES ('67af8e6d-20b4-4fe0-b921-058578bf68dd', 'оао рога и копыта', '{2-222-222,3-333-333}', '56fb6d1f-659d-4883-9f3b-7cd3fbf5bb58');
INSERT INTO public.organizations VALUES ('5e3c030c-d02c-43fa-b097-d162f80fb944', 'оао красивые люди', '{8-923-666-13-13}', '56fb6d1f-659d-4883-9f3b-7cd3fbf5bb58');


--
-- TOC entry 3297 (class 2606 OID 123079)
-- Name: activities activities_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

