from streamlit_l7 import l7
def renderChoroplethMap(geoData) :
    options = {
      "mapType": 'Map',
      "mapOptions": {
        "center": [120.210792, 30.246026],
        "zoom": 16,
      },
    
      "layers": [ 
          # {
          #       "type": 'raster',
          #       "source": { 
          #           "data": '//webrd01.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}',
          #           "parser": {"type": 'rasterTile', "tileSize": 256, "zoomOffset": 0},
          #       },
          #   },
                    
            {
              "type":'line',
              "source":{
                  "data":geoData
              },
              "autoFit": True,
              "shape": 'simple',
              "size": 1,
              "color":"#333",
        
            }
      ],
         
      "controls": [
          {
          "type": 'zoom',
          },{
            "type": 'scale',
          },{
            "type": 'fullscreen'
          }
      ],
  }
    l7(options=options, style={"height": 400}, key="streamlit-l7")
