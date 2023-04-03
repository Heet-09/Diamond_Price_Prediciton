import numpy as np
import pickle
import streamlit as st
import streamlit.components.v1 as components

# loading the saved model

loaded_model = pickle.load(open('diamond_model.sav','rb'))

# creating a function for Prediction

def diamond_prediction(input_data):
    

    # change the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data).astype(float)

    # reshape the numpy array as we are predicting for one datapoint
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    # prediction = loaded_model.predict(input_data)
    st.write("The value of diamond is ",prediction)

    # if (prediction[0] == 0):
    #     st.write('The cancer is Malignant')

    # else:
    #     st.write('The Cancer is Benign')

# def load_form(url):
#     components.iframe(url, width=700, height=700, scrolling=True)



  
def main():
    
    st.set_page_config(layout="wide")
    
    # giving a title
    st.title('Cancer Cell Classification Web APP')   
    
    

    
    col1, col2, col3 = st.columns(3)

    with col1:
        Carat=st.text_input('Carat')
        # Cut=st.text_input('Cut')
        cut_map = {'Ideal':1, 'Premium':2, 'Very Good':3, 'Good': 4, 'Fair':5}
        selected_cut = st.selectbox("Select cut ",options=list(cut_map.keys()))
        cut_value = cut_map[selected_cut]
        clarity_map = {'SI2': 1, 'SI1': 2, 'VS1': 3, 'VS2': 4, 'VVS2': 5, 'VVS1': 6, 'I1': 7, 'IF': 8}
        selected_clarity = st.selectbox("Select a Clarity", options=list(clarity_map.keys()))
        clarity_value = clarity_map[selected_clarity]
        # Clarity=st.text_input('Clarity')
    with col2:
        Depth=st.text_input('Depth')
        Table=st.text_input('Table')
        # Color=st.text_input('Color')
        color_dict = {'D': 7, 'E': 6, 'F': 5, 'G': 4, 'H': 3, 'I': 2, 'J': 1}
        selected_color = st.selectbox("Select a color", options=list(color_dict.keys()))
        color_value = color_dict[selected_color]
        # st.write(f"The corresponding value for color {selected_color} is {corresponding_value}")  
    with col3:
        x=st.text_input('X-dimensions')
        y=st.text_input('Y-dimensions')
        z=st.text_input('Z-dimensions')

    # code for Prediction
    values = ''
    
    # creating a button for Prediction
   
    if st.button('predict Value'):
        values = diamond_prediction([Carat,cut_value,clarity_value,Depth,Table,color_value,x,y,z])
        # diagnosis = cancer_prediction([mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimensions,radius_error,texture_error,perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,symmetry_error,fractal_dimensions_error,worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimensions])

    # st.success(values)


   
if __name__ == '__main__':
    main()


