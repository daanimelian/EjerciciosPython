def tiempo_a_minuto():
"""Le pide al usuario que ingrese dos intervalos expresados en horas minutos y segundos, y las suma"""
        h=int(input("Ingrese una cantidad de horas: "))
        m=int(input("Ingrese una cantidad de minutos: "))
        s=int(input("Ingrese una cantidad de segundos: "))
        h_2=int(input("Ingrese una cantidad de horas: "))
        m_2=int(input("Ingrese una cantidad de minutos: "))
        s_2=int(input("Ingrese una cantidad de segundos: "))
#Suma los segundos
        s_3 = s + s_2
        m_3=0
        seg = 0
#Si la suma da mas de 59, transforma los segundos en minutos
        if s_3 > 59:
               m_3 = s_3 // 60
               seg_h = s_3 % 60
               seg = s + s_2 - s_3 + seg_h
        m_4 = m + m_2 + m_3
        h_3 = 0
#Si la suma da mas de 59, transforma los minutos en horas
        if m_4 > 59:
               h_3 = m_4 // 60
               min_h = m_4 % 60
               minu = min_h 

        h_4 = 0
        h_4 = h_2 + h_3 + h
		print(" Son horas:", h_4,"Minutos:",minu , "Segundos:", seg, "totales")
