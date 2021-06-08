# Estimating the Velocity of Muldrow Glacier during a Surge Event using Synthetic Aperture Radar Imagery and Dense Optical Flow

In this project we tried three different approaches to get glacier velocities using Synthetic Aperture Radar (SAR) imagery in order to analyze the recent surge event at Muldrow Glacier. Dense Optical Flow was the most promising, and results from Dense Optical Flow along with Particle Image Velocimetry can be seen in our demo notebook titled "muldrow_analysis_final", and Spare Optical Flow can be seen in our demo notebook "Velocity_Tracking_Algorithm_Notebook_(Final)". Please also check out our final presentation "Final_Project_Poster". (version with active gifs here: https://docs.google.com/presentation/d/1uPHsNcp5WiOWXrHPpUaToPzx5WN8wBvEkCgr-bVGujI/edit#slide=id.p1) The team contract can be found in "team_contract".



## Organization 

    Hot_injection
        |- import_data
            |- import_glacier_shapefiles_rgi
                |- import_glacier_shapefiles.ipynb
                |- mt_rainier.geojson
                |- muldrow_glacier.geojson
            |- import_sar_asf_script
                |- sar_images_geocoded_cropped
                |- crop.ipynb
                |- download-all-2021-04-15_10-50-23.py
                |- geocode.ipynb
            |- import_sar_aws
                |- import_SAR.ipynb
                |- mean_trend.csv
                |- mean_trend_full_res.csv
                |- mt_rainier.geojson
                |- s3paths.txt
                |- stack10TES.vrt
        |- misc
            |- Sparse optical Flow.ipynb
            |- function.py
            |- hw3function.py
            |- muldrow_analysis.ipynb
            |- muldrow_timeseries.gif
            |- placeholder
        |- .gitignore
        |- Final_Project_Poster.pdf
        |- LICENSE
        |- README.md
        |- Velocity_Tracking_Algorithm_Notebook_(Final).ipynb
        |- muldrow_analysis_final.ipynb
        |- team_contract