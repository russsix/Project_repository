This is the description of the Group number 1.4, we will focus on making a tool that tells people their visa requirement for going on vacation and suggests them the cheaper prices.  
Additional file downloads
    To fully utilize the map functionality in this application, you need to download the `global_states.geojson` file.
    Download the File: Visit (https://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-0-countries/) and download the file to your local machine
    Place the File: Move the downloaded file to the `data/` directory within the cloned project repository
    Transform the file to json format 
    import geopandas
        gdf = gpd.read_file(r"D:\Download\ne_110m_admin_0_countries.shp")

    # Convert to GeoJSON and save to a file
    gdf.to_file(r"D:\Download\global_states.geojson", driver='GeoJSON')
