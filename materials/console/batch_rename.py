import os
import shutil
names = ["background_2fort", "background_gravelpit", "background_mvm", "background_upward", "background01", "background02", "title_blue", "title_invasion", "title_pyro_jungle_inferno_2017", "title_red", "title_summer_operation_2015", "title_team", "title_team_competitive", "title_team_heavy01_red", "title_team_heavy01_blu", "title_team_jungle_inferno_2017", "title_team_pyro01_blu", "title_team_pyro01_red", "title_team_tough_break", "title_war"]
        
for i in range(19):
    os.rename("alena_aenami_bg_%s.vtf" % i, names[i] + '.vtf')
    shutil.copy(names[i] + '.vtf', names[i] + '_widescreen.vtf')