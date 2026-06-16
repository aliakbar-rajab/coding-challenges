def calculateRAM(KE, d, detector):
    KE_J = KE * 1e-18
    d_m = d * 1e-3
    NA = 6.022e23
    mz_dict = {}
    for I, t in detector:
        t_s = t * 1e-9
        v = d_m / t_s
        m_kg = (2 * KE_J) / (v ** 2)
        m_g = m_kg * 1000
        
        raw_Ar = m_g * NA
        mz = round(raw_Ar * 2) / 2
        mz_dict[mz] = mz_dict.get(mz, 0) + I
    true_masses = {}
    
    for mz, I in mz_dict.items():
        if (mz * 2) in mz_dict and mz != 1.0:
            pass 
        else:
            true_masses[mz] = I
            
    for mz, I in mz_dict.items():
        if (mz * 2) in mz_dict and mz != 1.0:
            true_masses[mz * 2] += I
            
    total_mass_x_current = sum(mass * current for mass, current in true_masses.items())
    total_current = sum(true_masses.values())
    
    return total_mass_x_current / total_current