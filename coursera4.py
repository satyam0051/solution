def future_value(present_value,annual_rate,periods_per_year,years):
    rate_per_period=annual_rate/periods_per_year
    periods=periods_per_year*years
    fv=present_value*(1+rate_per_period)**periods
    return fv
    





print("$1000 at 2% compound daily for 4 years yield $",future_value(1000,.02,365,4)) 
