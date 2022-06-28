# GeneratingToursReportTurismoi
Download a server info and make a excel

// Se necesita realizar la siguiente consulta en el servidor de bases de datos... Deacuerdo al pais que se necesite

echo "select
       IFNULL(CONCAT(pck.id, '|'),'NULL|') as tour_id,
       IFNULL(CONCAT(pck.user_id, '|'),'NULL|') as tour_user_id,
       IFNULL(CONCAT(REPLACE(pck.name, '|', ' '), '|'),'NULL|') as tour_name,
       IFNULL(CONCAT(REPLACE(REPLACE(pck.description, '\r\n', ' '), '|', ' '), '|'), 'NULL|') as tour_description,
       IFNULL(CONCAT(REPLACE(REPLACE(pck.notes, '\r\n', ' '), '|', ' '), '|'), 'NULL|') as tour_notes,
       IFNULL(CONCAT(REPLACE(REPLACE(pck.includes, '\r\n', ' '), '|', ' '), '|'), 'NULL|') as tour_includes,
       IFNULL(CONCAT(REPLACE(REPLACE(pck.not_includes, '\r\n', ' '), '|', ' '), '|'), 'NULL|') as tour_not_includes,
       IFNULL(CONCAT(REPLACE(REPLACE(pck.starting_point, '|', ' '), '\r\n', ' '), '|'), 'NULL|') as tour_starter_point,
       IFNULL(CONCAT(pck.slug_es, '|'),'NULL|') as URL,
       IFNULL(CONCAT(pck.price, '|'), 'NULL|') as tour_price,
       IFNULL(CONCAT(REPLACE(REPLACE(pck.price_note, '|', ' '), '\r\n', ' '), '|'), 'NULL|') as tour_price_note,
       IFNULL(CONCAT(pck.children_price, '|'),'NULL|') as tour_child_price,
       IFNULL(CONCAT(pck.viality_from, '|'),'NULL|') as tour_viality_from,
       IFNULL(CONCAT(pck.viality_to, '|'),'NULL|') as tour_viality_to,
       IFNULL(CONCAT(pck.created_at, '|'),'NULL|') as tour_created_at,
       IFNULL(CONCAT(pck.updated_at, '|'),'NULL|') as tour_update_at,
       IFNULL(CONCAT(pck.days, '|'),'NULL|') as tour_days,
       IFNULL(CONCAT(pck.nights, '|'),'NULL|') as tour_nights,
       IFNULL(CONCAT(pck.state, '|'),'NULL|') as tour_state,
       IFNULL(CONCAT(pck.housing_type, '|'),'NULL|') as tour_hounsing_type,
       IFNULL(CONCAT(pck.country_id, '|'),'NULL|') as tour_country_id,
       IFNULL(CONCAT(pck.housing_name, '|'),'NULL|') as tour_housing_name,
       IFNULL(CONCAT(pck.stock, '|'),'NULL|') as tour_stock,
       IFNULL(CONCAT(pck.comission, '|'),'NULL|') as tour_commision,
       IFNULL(CONCAT(pck.in_home, '|'),'NULL|') as tour_in_home,
       IFNULL(CONCAT(pck.is_canatur, '|'),'NULL|') as tour_is_canatour,
       IFNULL(CONCAT(pck.blocked, '|'),'NULL|') as tour_blocked,
       IFNULL(CONCAT(pck.adult_foreigner_price, '|'),'NULL|') as tour_adult_foreigner_price,
       IFNULL(CONCAT(pck.children_foreigner_price, '|'),'NULL|') as tour_child_foreigner_price,
       IFNULL(CONCAT(pck.purchase_time, '|'),'NULL|') as tour_purchase_time,
       IFNULL(CONCAT(pck.min_passenger, '|'),'NULL|') as tour_min_passenger,
       IFNULL(CONCAT(pck.published_on, '|'),'NULL|') as tour_published_on,
       IFNULL(CONCAT(REPLACE(pck.name_en, '|', ' '), '|'),'NULL|') as tour_name_en,
       IFNULL(CONCAT(pck.translation_mode, '|'),'NULL|') as tour_translation_mode,
       IFNULL(CONCAT(pck.list_price, '|') ,'NULL|') as tour_list_price,
       IFNULL(CONCAT(pck.duration_in_hours, '|'),'NULL|') as tour_duration_in_hours,
       IFNULL(CONCAT(pck.language, '|'),'NULL|') as tour_language,
       IFNULL(CONCAT(pck.start_time, '|'),'NULL|') as tour_start_time,
       IFNULL(CONCAT(pck.cancellation_policy, '|'),'NULL|') as tour_cancellation_policy,
       IFNULL(CONCAT(pck.reservations_count, '|') ,'NULL|') as tour_reservations_count,
       IFNULL(CONCAT(pck.turismoi_network, '|'),'NULL|') as turismoi_network,
       IFNULL(CONCAT(pck.saas_network, '|'),'NULL|') as saas_network,
       IFNULL(CONCAT(usr.commercial_name, '|') ,'NULL|') as tour_operador_name,
       IFNULL(CONCAT(rt.state, '|'),'NULL|')  as payment_type
from
    packages pck left join reservations rt
on pck.id = rt.package_id
inner join users usr
on pck.user_id = usr.id;" | mysql -u y20 -p -h 10.41.131.22 --default-character-set=utf8 turismoi_db_cl > ventas_chile_2022_jun_v3.csv


ojo: que termine con salto de linea

Meterlo en la carperta data.
Darle al boton load.

Darle al btn save para generar el excel.

La fila queda guardada en la carpeta output

// Pasela por el limpiador de archivos TOOLS/CLEANER
__________________________________

Para los otros paises la consulta cambia: // Consulta desactualizada... Hay que Actualizar.

echo "select 
       IFNULL(CONCAT(pck.id, '|'),'NULL|') as tour_id,
       IFNULL(CONCAT(pck.user_id, '|'),'NULL|') as tour_user_id,
       IFNULL(CONCAT(REPLACE(pck.name, '|', ' '), '|'),'NULL|') as tour_name,
       IFNULL(CONCAT(REPLACE(REPLACE(pck.starting_point, '|', ' '), '\r\n', ' '), '|'), 'NULL|') as tour_starter_point,
	   CONCAT(pck.host_country_iso, '|') as country,
       IFNULL(CONCAT(pck.slug_es, '|'),'NULL|') as URL,
       IFNULL(CONCAT(pck.price, '|'), 'NULL|') as tour_price,
       IFNULL(CONCAT(pck.children_price, '|'),'NULL|') as tour_child_price,
       IFNULL(CONCAT(pck.viality_from, '|'),'NULL|') as tour_viality_from,
       IFNULL(CONCAT(pck.viality_to, '|'),'NULL|') as tour_viality_to,
       IFNULL(CONCAT(pck.created_at, '|'),'NULL|') as tour_created_at,
       IFNULL(CONCAT(pck.updated_at, '|'),'NULL|') as tour_update_at,
       IFNULL(CONCAT(pck.days, '|'),'NULL|') as tour_days,
       IFNULL(CONCAT(pck.nights, '|'),'NULL|') as tour_nights,
       IFNULL(CONCAT(pck.state, '|'),'NULL|') as tour_state,
       IFNULL(CONCAT(pck.housing_type, '|'),'NULL|') as tour_hounsing_type,
       IFNULL(CONCAT(pck.country_id, '|'),'NULL|') as tour_country_id,
       IFNULL(CONCAT(pck.housing_name, '|'),'NULL|') as tour_housing_name,
       IFNULL(CONCAT(pck.stock, '|'),'NULL|') as tour_stock,
       IFNULL(CONCAT(pck.comission, '|'),'NULL|') as tour_commision,
       IFNULL(CONCAT(pck.in_home, '|'),'NULL|') as tour_in_home,
       IFNULL(CONCAT(pck.is_canatur, '|'),'NULL|') as tour_is_canatour,
       IFNULL(CONCAT(pck.blocked, '|'),'NULL|') as tour_blocked,
       IFNULL(CONCAT(pck.adult_foreigner_price, '|'),'NULL|') as tour_adult_foreigner_price,
       IFNULL(CONCAT(pck.children_foreigner_price, '|'),'NULL|') as tour_child_foreigner_price,
       IFNULL(CONCAT(pck.purchase_time, '|'),'NULL|') as tour_purchase_time,
       IFNULL(CONCAT(pck.min_passenger, '|'),'NULL|') as tour_min_passenger,
       IFNULL(CONCAT(pck.published_on, '|'),'NULL|') as tour_published_on,
       IFNULL(CONCAT(REPLACE(pck.name_en, '|', ' '), '|'),'NULL|') as tour_name_en,
       IFNULL(CONCAT(pck.translation_mode, '|'),'NULL|') as tour_translation_mode,
       IFNULL(CONCAT(pck.list_price, '|') ,'NULL|') as tour_list_price,
       IFNULL(CONCAT(pck.duration_in_hours, '|'),'NULL|') as tour_duration_in_hours,
       IFNULL(CONCAT(pck.language, '|'),'NULL|') as tour_language,
       IFNULL(CONCAT(pck.start_time, '|'),'NULL|') as tour_start_time,
       IFNULL(CONCAT(pck.cancellation_policy, '|'),'NULL|') as tour_cancellation_policy,
       IFNULL(CONCAT(pck.reservations_count, '|') ,'NULL|') as tour_reservations_count,
       IFNULL(CONCAT(pck.turismoi_network, '|'),'NULL|') as turismoi_network,
       IFNULL(CONCAT(pck.saas_network, '|'),'NULL|') as saas_network,
       IFNULL(CONCAT(usr.commercial_name, '|') ,'NULL|') as tour_operador_name,
       IFNULL(CONCAT(rt.state, '|'),'NULL|')  as payment_type
from
    packages pck left join reservations rt
on pck.id = rt.package_id
inner join users usr
on pck.user_id = usr.id;" | mysql -u turismoi -p -h 10.41.131.22 --default-character-set=utf8 turismoi_prod > otros.csv



ojo: que termine con salto de linea
