from ipywidgets import interact, interactive, fixed, interact_manual, HBox, VBox, IntSlider, Play, jslink, Tab
import ipywidgets as widgets
from file_browser import SelectFilesButton
import os
# UX

workingdir_selector = widgets.Text(
	value=os.getcwd(),
	placeholder=os.getcwd(),
	#description='Working Directory:',
	layout=widgets.Layout(width='35%'),
	disabled=False
)

wkdir_browser_btn = SelectFilesButton(desc='Browse')

workingdir_btn = widgets.Button(
	description='Set WkDir',
	disabled=False,
	button_style='success', # 'success', 'info', 'warning', 'danger' or ''
	tooltip='Set working directory'
)
context_path_txt = widgets.Text(
	value=os.getcwd(),
	placeholder=os.getcwd(),
	#description='Load Context from:',
	layout=widgets.Layout(width='35%'),
	disabled=False
)
context_load_btn = widgets.Button(
	description='Load Context',
	disabled=False,
	button_style='success', # 'success', 'info', 'warning', 'danger' or ''
	tooltip='Load Context'
)
context_save_btn = widgets.Button(
	description='Save Context',
	disabled=False,
	button_style='success', # 'success', 'info', 'warning', 'danger' or ''
	tooltip='Save Context'
)


#####
file_selector = widgets.Text(
	value=os.getcwd(),
	placeholder=os.getcwd(),
	description='File/Folder Path:',
	layout=widgets.Layout(width='50%'),
	disabled=False
)
load_files_btn = widgets.Button(
	description='Load Files',
	disabled=False,
	button_style='success', # 'success', 'info', 'warning', 'danger' or ''
	tooltip='Load Files',
	icon='check'
)

#####

is_batch_widget = widgets.ToggleButtons(
	options=['Group', 'Independent'],
	description='Grouped?:',
	disabled=False,
	button_style='', # 'success', 'info', 'warning', 'danger' or ''
	tooltips=['Run all movies together as if one movie', 'Run each movie independently'],
#     icons=['check'] * 3
)
dslabel = widgets.Label(value="Downsample Percentage (height, width, frames/time)")
ds_layout = widgets.Layout(width="20%")
dsx_widget = widgets.BoundedFloatText(
	value=1,
	min=0.1,
	max=1.0,
	step=0.1,
	description='height:',
	disabled=False,
	layout=ds_layout
)
dsy_widget = widgets.BoundedFloatText(
	value=1,
	min=0.1,
	max=1.0,
	step=0.1,
	description='width:',
	disabled=False,
	layout=ds_layout
)
dst_widget = widgets.BoundedFloatText(
	value=1,
	min=0.1,
	max=1.0,
	step=0.1,
	description='frames:',
	disabled=False,
	layout=ds_layout
)

#####

gSigFilter_widget = widgets.IntSlider(
	value=7,
	min=0,
	max=50,
	step=1,
	description='High Pass Filter:',
	disabled=False,
	continuous_update=False,
	orientation='horizontal',
	readout=True,
	readout_format='d',
	tooltip='Gaussian Filter Size (1p data only)'
)

max_shifts_widget = widgets.BoundedFloatText(
	value=6,
	min=1,
	max=100,
	step=1,
	description='Max Shifts:',
	disabled=False,
	layout=ds_layout
)

is_rigid_widget = widgets.ToggleButtons(
	options=['Rigid', 'Non-Rigid'],
	description='MC Mode:',
	disabled=False,
	button_style='warning', # 'success', 'info', 'warning', 'danger' or ''
	tooltips=['Rigid correction (faster)', 'Non-rigid correction (slow, more accurate)'],
#     icons=['check'] * 3
)


######
run_mc_btn = widgets.Button(
	description='Run Motion Correction',
	disabled=False,
	button_style='info', # 'success', 'info', 'warning', 'danger' or ''
	tooltip='Run motion correction',
	layout=widgets.Layout(width="30%")
)

######



####

play_mov_btn = widgets.Button(
	description='Play Movies',
	disabled=False,
	button_style='success', # 'success', 'info', 'warning', 'danger' or ''
	tooltip='Play Movies'
)

correlation_plot_btn = widgets.Button(
	description='Inspect Correlation Plot',
	disabled=False,
	button_style='success', # 'success', 'info', 'warning', 'danger' or ''
	tooltip='Inspect Correlation Plot'
)

#########  CNMF widgets

#tab_contents = ['P0', 'P1', 'P2', 'P3', 'P4']
#children = [widgets.Text(description=name) for name in tab_contents]
#tab = widgets.Tab()
#tab.children = children


cnmf_file_selector = widgets.Text(
	value=os.getcwd(),
	placeholder=os.getcwd(),
	description='File (.mmap):',
	layout=widgets.Layout(width='50%'),
	disabled=False
)


#####


is_patches_widget = widgets.ToggleButtons(
	value='Single FOV',
	options=['Patches', 'Single FOV'],
	description='Patches?:',
	disabled=False,
	button_style='', # 'success', 'info', 'warning', 'danger' or ''
	tooltips=['Run each frame in parallel by breaking into overlapping FOVs', 'The whole frame is analyed as a single FOV'],
#     icons=['check'] * 3
)
dslabel = widgets.Label(value="Downsample Percentage (spatial, temporal)")
ds_layout = widgets.Layout(width="20%")
ds_spatial_widget = widgets.BoundedFloatText(
	value=1.0,
	min=0.0,
	max=1.0,
	step=0.1,
	description='spatial:',
	disabled=False,
	layout=ds_layout
)
ds_temporal_widget = widgets.BoundedFloatText(
	value=1.0,
	min=0.0,
	max=1.0,
	step=0.1,
	description='temporal:',
	disabled=False,
	layout=ds_layout
)

####


k_widget = widgets.BoundedIntText(
	value=100,
	min=1,
	max=1000,
	step=5,
	description='K:',
	tooltip='Expected # Cells (Per Patch)',
	disabled=False,
	layout=ds_layout
)
gSig_widget = widgets.BoundedIntText(
	value=4,
	min=1,
	max=50,
	step=1,
	description='gSig:',
	tooltip='Gaussian Kernel Size',
	disabled=False,
	layout=ds_layout
)
gSiz_widget = widgets.BoundedIntText(
	value=12,
	min=1,
	max=50,
	step=1,
	description='gSiz:',
	tooltip='Average Cell Diamter',
	disabled=False,
	layout=ds_layout
)

stride_widget = widgets.BoundedIntText(
	value=20,
	min=1,
	max=50,
	step=1,
	description='Stride:',
	tooltip='Stride',
	disabled=False,
	layout=ds_layout
)

rf_widget = widgets.BoundedIntText(
	value=40,
	min=1,
	max=75,
	step=1,
	description='Patch Size:',
	tooltip='Patch Size',
	disabled=False,
	layout=ds_layout
)

######

min_corr_widget = widgets.FloatSlider(
	value=0.85,
	min=0.0,
	max=1.0,
	step=0.05,
	description='Min. Corr.:',
	disabled=False,
	continuous_update=False,
	orientation='horizontal',
	readout=True,
	readout_format='.2',
	tooltip='Minimum Correlation'
)
min_pnr_widget = widgets.IntSlider(
	value=15,
	min=1,
	max=50,
	step=1,
	description='Min. PNR.:',
	disabled=False,
	continuous_update=False,
	orientation='horizontal',
	readout=True,
	readout_format='d',
	tooltip='Minimum Peak-to-Noise Ratio'
)

deconv_flag_widget = widgets.Checkbox(
	value=False,
	description='Run Deconvolution',
	disabled=False,
	tooltip='The oasis deconvolution algorithm will run along with CNMF',
	layout=widgets.Layout(width="30%")
)

save_movie_widget = widgets.Checkbox(
	value=False,
	description='Save Denoised Movie (.avi)',
	disabled=False,
	tooltip='Saves a background-substracted and denoised movie',
	layout=widgets.Layout(width="30%")
)

#####

run_cnmf_btn = widgets.Button(
	description='Run CNMF-E',
	disabled=False,
	button_style='info', # 'success', 'info', 'warning', 'danger' or ''
	tooltip='Run CNMF-E',
	layout=widgets.Layout(width="30%")
)

####


#delete/refine ROIs control, and save data
delete_roi_btn = widgets.Button(
	description='Delete ROI',
	disabled=False,
	button_style='warning', # 'success', 'info', 'warning', 'danger' or ''
	tooltip='Exclude ROI'
)
delete_list_widget = widgets.SelectMultiple(
	options=[],
	value=[],
	rows=3,
	description='Exclud. ROIs',
	disabled=False,
	layout=widgets.Layout(width="18%")
)
download_btn = widgets.Button(
	description='Download Data',
	disabled=False,
	button_style='info', # 'success', 'info', 'warning', 'danger' or ''
	tooltip='Download fluorescence traces as CSV file'
)
dff_chk = widgets.Checkbox(
	value=False,
	description='Use dF/F',
	disabled=False,
	tooltip='Compute the delta F/F values',
	layout=widgets.Layout(width="25%")
)


#####


deconv_chk = widgets.ToggleButtons(
    options=['Signal', 'Deconvolution', 'Both'],
    description='Plot options:',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltips=['Denoised/demixed Ca2+ signal', 'Deconvolved Ca2+ signal', 'Plot both'],
	layout=widgets.Layout(width="18%"),
)

#####
#children = []
#for i in range(len(children)):
#    tab.set_title(i, str(i))
#tab

view_cnmf_results_widget = widgets.Button(
	description='View/Refine CNMF Results',
	disabled=False,
	button_style='info', # 'success', 'info', 'warning', 'danger' or ''
	tooltip='View CNMF Results',
	layout=widgets.Layout(width="30%")
)

##### Validation Tab: ######
############################

validate_col_mag_slider = widgets.IntSlider(
	value=2,
	min=1,
	max=10,
	step=1,
	description='Movie Magnification:',
	disabled=False,
	continuous_update=False,
	orientation='horizontal',
	readout=True,
	readout_format='d',
	tooltip='How much to magnify the movie',
	layout=widgets.Layout(width="30%")
)

validate_col_cnmf_mov_btn = widgets.Button(
	description='View CNMF-E Analyzed Movie',
	disabled=False,
	button_style='info', # 'success', 'info', 'warning', 'danger' or ''
	tooltip='View Background Movie',
	layout=widgets.Layout(width="30%")
)

validate_col_bgmov_btn = widgets.Button(
	description='View Background Movie',
	disabled=False,
	button_style='info', # 'success', 'info', 'warning', 'danger' or ''
	tooltip='View Background Movie',
	layout=widgets.Layout(width="30%")
)

validate_col_residual_btn = widgets.Button(
	description='View Residual Movie',
	disabled=False,
	button_style='info', # 'success', 'info', 'warning', 'danger' or ''
	tooltip='View Residual Movie',
	layout=widgets.Layout(width="30%")
)

#log/console:
log_widget = widgets.Textarea(
    value='',
    description='Console:',
    disabled=False,
	layout=widgets.Layout(width="60%", height="100px")
)

#####
