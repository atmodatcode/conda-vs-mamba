from Magics import macro as magics

#name = 'magics'
#Setting of the output file name
output = magics.output(output_formats = ['png'],
             output_name_first_page_number = "off",
             output_name = "mymagicsplot")


#Import the  data
data =  magics.mnetcdf(netcdf_filename="test.nc", netcdf_value_variable="aps")


#Apply styling
legend = magics.mlegend()
contour = magics.mcont( contour_shade                     = "on",
                        contour_shade_method              = "area_fill",
                        legend='on')
coast = magics.mcoast()

# Make the plot
magics.plot(output, data, contour, coast, legend) 
