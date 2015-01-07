perfometers["check_mk-cvadmin_stat.df"] = perfometer_check_mk_df

def perfometer_check_mk_cvadmin_stat_info(row, check_command, perf_data):
	color = { 0: "#6fc", 1: "#ffc", 2: "#f66", 3: "#fc0" }[row["service_state"]]
	return "%d" % int(perf_data[0][1]), perfometer_logarithmic(perf_data[0][1], 20, 2, color)

perfometers["check_mk-cvadmin_stat.info"] = perfometer_check_mk_cvadmin_stat_info
