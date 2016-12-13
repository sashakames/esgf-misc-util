import sys
import json


if len(sys.argv) == 1:
  print "Usage:"
  print  "     python CV2ini.py <project-name> <base-path> > <output-file>"
  print
  print "where <base-path> is the location of the CV repo"
  exit(0)


project_in = sys.argv[1]
base_path_in = sys.argv[2]


# TODO : hardcoded values to be replaced by input .json files

facet_dict = { "activity": "activity_id", 
               "institute": "institution_id",
               "model": "source_id", 
               "experiment": "", 
               "ensemble": "", 
               "cmor_table": "table_id", 
               "variable": "", 
               "grid_label": "grid_label",
               "version": "" }


DRS_list = [ "activity",  
               "institute",
               "model",
               "experiment",
               "ensemble",
               "cmor_table",
               "variable",
               "grid_label",
               "version" ]


delimited_facets = { "realm": "space"}

def print_delimited():

    for x in delimited_facets:

        print x + "_delimiter = " + delimited_facets[x]




extract_global_attrs = [  "realm", "frequency", "product", "mip_era", "grid_resolution" ]

def print_extract_attrs():

    print "extract_global_attrs = " + ', '.join(extract_global_attrs)


def gen_models_table_entries_and_print(base_path, project):
    

    f=open(base_path + "/" + project + "_source_id.json")

    sidjobj = json.loads(f.read())
    f.close()

    f=open(base_path + "/" + project + "_institution_id.json")
    

    insts = json.loads(f.read())
    f.close()

    outf = open("esgcet_models_table.part.txt", "w")

    print "model_options = " + ', '.join(sidjobj["source_id"].keys())

    print "institute_options = " + ', '.join(insts["institution_id"].keys())

    for key in sidjobj["source_id"].keys():


        child = sidjobj["source_id"][key]

        src_str = child["label_extended"]

        inst_keys = child["institution_id"]
          
        
        inst_arr = []

        for n in inst_keys:

            inst_arr.append(insts["institution_id"][n])



        outarr = [project, key, " ", ', '.join(inst_arr) + ", " + src_str]

        outf.write('  ' +  ' | '.join(outarr) + "\n")
    outf.close()
    

def get_facet_list(first_item, vers):

    outarr = [first_item]

    for x in DRS_list:
        
        if (vers or (x != "version")):

            outarr.append("%(" + x + ")s")

    return outarr

def print_directory_format():

    outarr = get_facet_list("/%(root)s/%(project)s", True)


    print "directory_format = " + '/'.join(outarr)



def print_dataset_id_fmt():
    
    outarr = get_facet_list("%(project)s", False)
    
    print "dataset_id_format = " + '.'.join(outarr)


def write_options_list(base_path, project, facet_in, facet_out):

    f=open(base_path + "/" + project + "_" + facet_in + ".json")

    jobj = json.loads(f.read())[facet_in]
    
    print facet_out + "_options = " + ', '.join(jobj)


def write_experiment_options(base_path, project):

    f=open(base_path + "/" + project + "_experiment_id.json")
    
    jobj = json.loads(f.read())["experiment_id"]

    print "experiment_options ="
    for key in jobj:

        print "  " +  project + " | " + key + " | " + jobj[key]["description"].replace('%', "pct")


def write_categories():

#    f = open(ext_file)

    print "categories ="
    print "  project  | enum | true | true | 0"


    alt_forms = []


    for i, facet_out in enumerate(facet_dict):
        
        type_str = "enum"

        if facet_out == "ensemble":
            type_str = "string"

        outarr = [facet_out, type_str, "true", "true" , str(i + 1)  ]
        
        conv = facet_dict[facet_out]

        if len(conv) > 0 and conv != facet_out:
            alt_forms.append(conv)



        print "   " + ' | '.join(outarr)

    base = len(facet_dict) + 1

    for i, facet_out in enumerate(alt_forms):
    
        outarr = [facet_out, "string", "false", "true" , str(i + base)  ]
        print "   " + ' | '.join(outarr)

    print "  description  | text | false | false | 99"

print "[project:" + project_in + "]"



write_categories()

print "category_defaults ="
print "    project | CMIP6"


gen_models_table_entries_and_print(base_path_in, project_in)
write_experiment_options(base_path_in, project_in)


# TODO get options list
for f_out in ["activity", "cmor_table", "grid_label"]:

    
    f_in = facet_dict[f_out]

    if len(f_in) == 0:
        f_in = f_out


    write_options_list(base_path_in, project_in, f_in, f_out)    



print "dataset_name_format = project=%(project_description)s, model=%(model_description)s, experiment=%(experiment_description)s, time frequency=%(frequency)s, modeling realm=%(realm)s, ensemble=%(ensemble)s, version=%(version)s"

print "ensemble_pattern = r%(digit)si%(digit)sp%(digit)sf%(digit)s"

print_directory_format()
print_dataset_id_fmt()



print "las_configure = true" 

print "thredds_exclude_variables = a, a_bnds, alev1, alevel, alevhalf, alt40, b, b_bnds, basin, bnds, bounds_lat, bounds_lon, dbze, depth, depth0m, depth100m, depth_bnds, geo_region, height, height10m, height2m, lat, lat_bnds, latitude, latitude_bnds, layer, lev, lev_bnds, location, lon, lon_bnds, longitude, longitude_bnds, olayer100m, olevel, oline, p0, p220, p500, p560, p700, p840, plev, plev3, plev7, plev8, plev_bnds, plevs, pressure1, region, rho, scatratio, sdepth, sdepth1, sza5, tau, tau_bnds, time, time1, time2, time_bnds, vegtype"

print "variable_locate = ps, ps_"

print "variable_per_file = true"

print "version_by_date = true"

print "min_cmor_version = 3.2.0"  

print "project_handler_name = cmip6_handler:CMIP6Handler"

print "realm_delimiter = space"

print "min_cf_version = 1.6"

print "cmor_table_path = /usr/local/"

print_delimited()

print_extract_attrs()
