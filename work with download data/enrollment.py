import pandas as pd
if __name__ == "__main__":
    data = pd.read_csv('CRDC2013_14content.csv')
    data['total_enrollment'] = data['TOT_ENR_M'] + data['TOT_ENR_F']
    all_enrollment = data['total_enrollment'].sum()
    tot_m = data['TOT_ENR_M'].sum()/all_enrollment
    tot_f = data['TOT_ENR_F'].sum()/all_enrollment
    sch_enr_hi =data['SCH_ENR_HI_M'].sum()+data['SCH_ENR_HI_F'].sum()
    sch_enr_hi = sch_enr_hi/all_enrollment
    sch_enr_am = data['SCH_ENR_AM_M'].sum()+data['SCH_ENR_AM_F'].sum()
    sch_enr_am = sch_enr_am/all_enrollment
    sch_enr_as = data['SCH_ENR_AS_M'].sum()+data['SCH_ENR_AS_F'].sum()
    sch_enr_as = sch_enr_as/all_enrollment
    sch_enr_hp = data['SCH_ENR_HP_M'].sum()+data['SCH_ENR_HP_F'].sum()
    sch_enr_hp = sch_enr_hp/all_enrollment
    sch_enr_bl = data['SCH_ENR_BL_M'].sum()+data['SCH_ENR_BL_F'].sum()
    sch_enr_bl = sch_enr_bl/all_enrollment
    sch_enr_wh = data['SCH_ENR_WH_M'].sum()+data['SCH_ENR_WH_F'].sum()
    sch_enr_wh = sch_enr_wh/all_enrollment
    sch_enr_tr = data['SCH_ENR_TR_M'].sum()+data['SCH_ENR_TR_F'].sum()
    sch_enr_tr = sch_enr_tr/all_enrollment
    print(tot_m)
    print(tot_f)
    print(sch_enr_hi)
    print(sch_enr_am)
    print(sch_enr_as)
    print(sch_enr_hp)
    print(sch_enr_bl)
    print(sch_enr_wh)
    print(sch_enr_tr)