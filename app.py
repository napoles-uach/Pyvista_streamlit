import streamlit as st
import streamlit.components.v1 as components
import pyvista
from pyvista import examples
pyvista.start_xvfb()
mesh = examples.load_uniform()
pl = pyvista.Plotter(shape=(1,2))
_ = pl.add_mesh(mesh, scalars='Spatial Point Data', show_edges=True)
pl.subplot(0,1)
_ = pl.add_mesh(mesh, scalars='Spatial Cell Data', show_edges=True)
pl.export_html('pyvista.html')  # doctest:+SKIP

option=st.sidebar.radio('Pyvista',('On','Off'))
if option=='On':
  HtmlFile = open("pyvista.html", 'r', encoding='utf-8')
  source_code = HtmlFile.read() 
  components.html(source_code, height = 500,width=500)
