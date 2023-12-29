
import os
import sys
import json
from PIL import Image
from io import BytesIO
project_root = os.path.abspath('./rendermap')
sys.path.append(project_root)
from rendermap import renderChoroplethMap
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_l7 import l7
import osmnx as osm

st.info("数据获取中……")
fivekm_buffer_nw = osm.graph_from_point((30.27,120.18), dist=500)
# fivekm_buffer_nw = osm.graph_from_place('hangzhou china',network_type='drive')

fig, ax = osm.plot_graph(fivekm_buffer_nw, show=False, close=False,node_size=0)

# Save the plot as an image in memory (BytesIO)
image_stream = BytesIO()
fig.savefig(image_stream, format='png', bbox_inches='tight', pad_inches=0.1)
plt.close(fig)  # Close the figure to release resources

# Display the image in Streamlit
st.image(image_stream, caption='OSM Street Network Graph', use_column_width=True)

# Display the image in Streamlit

# fivekm_buffer_nw = osm.graph_from_place('hangzhou china',network_type='drive')
fivekm_buffer_edges = osm.graph_to_gdfs(fivekm_buffer_nw,nodes=False, 
                                          edges=True)
st.success("数据获取完成!")
st.markdown('## Road Map')

def has_geo_interface(obj):
    return hasattr(obj, "__geo_interface__")

def records_from_geo_interface(data):
    """Un-nest data from object implementing __geo_interface__ standard"""
    flattened_records = []
    for d in data.__geo_interface__.get("features"):
        record = d.get("properties", {})
        geom = d.get("geometry", {})
        record["geometry"] = geom
        flattened_records.append(record)
    return flattened_records
# st.write('has_geo_interface',has_geo_interface(fivekm_buffer_edges))

# flattened_records = records_from_geo_interface(fivekm_buffer_edges)
# st.table(flattened_records)

data = fivekm_buffer_edges.to_json()



# 添加下载按钮
if st.button('Download Data as GeoJSON'):
    # 当按钮被点击时，将数据保存为 CSV 文件并提供下载链接
    st.download_button(label='Download CSV', data=data, file_name='road.json', key='road_download')

renderChoroplethMap(json.loads(data))
