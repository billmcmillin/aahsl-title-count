/*

PASS 1 - AAHSL title count query

Full data set requires two queries: *pass1, *pass2. Run queries in pgAdmin3, output to .tsv, and combine files manually.

** Be sure to set the current fiscal year on line 96 **

*/

SELECT DISTINCT ON (init.record_num) init.record_num, uni.field_content AS uniform, t.field_content AS title, issn.field_content as issn

FROM

	(SELECT i.id, i.record_num
		
		FROM

		(

		SELECT bibvar.record_id
		FROM
		sierra_view.varfield bibvar
		WHERE bibvar.marc_tag LIKE '65%'
		AND bibvar.marc_ind2 = '2'
		
		UNION
		
		SELECT olink.bib_record_id
		
			FROM
			sierra_view.order_record_cmf ord
		
			LEFT OUTER JOIN sierra_view.fund_master ofund ON (CAST(ord.fund_code AS integer) = ofund.code_num)
			JOIN sierra_view.bib_record_order_record_link olink ON (ord.order_record_id = olink.order_record_id)
			WHERE ofund.code LIKE 'h%'
		
		UNION
		
		SELECT bibloc.bib_record_id
			FROM
			sierra_view.bib_view hi
			JOIN sierra_view.bib_record_location bibloc ON (hi.id = bibloc.bib_record_id)
			WHERE bibloc.location_code LIKE 'bh%'
		
		UNION
		
		SELECT DISTINCT link.bib_record_id
			
			FROM
			
			sierra_view.item_view item
			LEFT JOIN sierra_view.item_record_property call ON (item.id = call.item_record_id)
			JOIN sierra_view.bib_record_item_record_link link ON (item.id = link.item_record_id)
			
			WHERE call.call_number_norm BETWEEN 'ta  164.00' and 'ta  164.99'
			OR call.call_number_norm BETWEEN 'tp  248.00' and 'tp  248.27'
			OR call.call_number_norm BETWEEN 'kf  480.00' and 'kf  480.50'
			OR call.call_number_norm BETWEEN 'kf  481.00' and 'kf  481.00'
			OR call.call_number_norm BETWEEN 'kf 3861.00' and 'kf 3896.00'
			OR call.call_number_norm BETWEEN 'hg 9371.00' and 'hg 9399.00'
			OR call.call_number_norm BETWEEN 'kf 1183.00' and 'kf 1189.00'
			OR call.call_number_norm BETWEEN 'kf 3515.00' and 'kf 3515.30'
			OR call.call_number_norm BETWEEN 'kf 2905.00' and 'kf 2915.00'
			OR call.call_number_norm BETWEEN 'kf 3760.00' and 'kf 3771.00'
			OR call.call_number_norm BETWEEN 'kf 3821.00' and 'kf 3845.00'
			OR call.call_number_norm BETWEEN 'kf 3775.00' and 'kf 3816.00'
			OR call.call_number_norm BETWEEN 'qh  345.00' and 'qh  499.00'
			OR call.call_number_norm BETWEEN 'qr    0.00' and 'qr  502.99'
			OR call.call_number_norm BETWEEN 'qh  201.00' and 'qh  278.00'
			OR call.call_number_norm BETWEEN 'qd  415.00' and 'qd  449.00'
			OR call.call_number_norm BETWEEN 'ge    0.00' and 'ge  350.99'
			OR call.call_number_norm BETWEEN 'qm    0.00' and 'qm  699.99'
			OR call.call_number_norm BETWEEN 'qp  500.00' and 'qp  801.00'
			OR call.call_number_norm BETWEEN 'qp  351.00' and 'qp  499.99'
			OR call.call_number_norm BETWEEN 'qp    0.00' and 'qp  349.00'
			OR call.call_number_norm BETWEEN 'qp  350.00' and 'qp  350.00'
			OR call.call_number_norm BETWEEN 'hv 1500.00' and 'hv 3024.99'
			OR call.call_number_norm BETWEEN 'hv 6626.00' and 'hv 6626.79'
			OR call.call_number_norm BETWEEN 'hq 1060.00' and 'hq 1073.99'
			OR call.call_number_norm BETWEEN 'hv    0.00' and 'hv 1499.00'
			OR call.call_number_norm BETWEEN 'hv 3025.00' and 'hv 4999.99'
			OR call.call_number_norm BETWEEN 'vg 2000.00' and 'vg 2005.99'
			OR call.call_number_norm BETWEEN 'hv 5000.00' and 'hv 5999.99'
			OR call.call_number_norm BETWEEN 'ha    0.00' and 'ha 4737.99'

			) items

		JOIN sierra_view.bib_view i ON (items.record_id = i.id)
		LEFT JOIN sierra_view.control_field y006 ON (i.id = y006.record_id AND y006.control_num = 6 AND y006.p00 = 's')
		LEFT JOIN sierra_view.bib_record_location bibloc ON (i.id = bibloc.bib_record_id)
		WHERE 
	
		i.bcode3 != 'd' AND i.bcode3 != 's'
	
		AND  (i.bcode2 = 's' OR (i.bcode2 = 'm' AND y006.p00 = 's'))
	
		AND i.cataloging_date_gmt <= '2017-06-30' -- cat date falls on or before last day of fiscal year
		AND (bibloc.location_code = 'bcdrom'
		OR bibloc.location_code = 'bcler' 
		OR bibloc.location_code = 'bcint' 
		OR bibloc.location_code = 'brwc' 
		OR bibloc.location_code = 'brint' 
		OR bibloc.location_code LIKE 'bdp%' 
		OR bibloc.location_code LIKE 'bh%' 
		OR bibloc.location_code LIKE 'bm%' 
		OR bibloc.location_code = 'bolin' 
		OR bibloc.location_code LIKE 'bu%')

	) init

LEFT JOIN sierra_view.varfield uni ON (init.id = uni.record_id AND uni.marc_tag = '130')
LEFT JOIN sierra_view.varfield t ON (init.id = t.record_id AND t.marc_tag = '245')
LEFT JOIN sierra_view.varfield issn ON (init.id = issn.record_id AND issn.marc_tag = '022')
