import ipywidgets as widgets

out = widgets.Output(layout={'border': '1px solid black', 'height':'100px'})

status_bar_widget = widgets.HTML(
    value="Idle",
    #placeholder='Status',
    description='<b>Status:</b>',
	layout=widgets.Layout(width="90%")
)
