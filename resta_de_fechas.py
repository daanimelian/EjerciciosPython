def cuantos_dias_pasaron(dia1, mes1, año1, dia2, mes2, año2):
	dias_totales = dia2 - dia1
	meses_totales = mes2 - mes1
	años_totales = año2 - año1
	if meses_totales < 0:
		meses_totales+=12
		años_totales-=1
	if años_totales < 0:
		meses_totales=12-abs(meses_totales)
		años_totales+=1
		
	print("Han pasado", abs(dias_totales), "dias", (meses_totales), "meses", abs(años_totales), "años")