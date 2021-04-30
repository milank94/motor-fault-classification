# jupyter extensions
jupyter nbextension enable --py widgetsnbextension; \
echo 'c.NotebookApp.contents_manager_class = "jupytext.TextFileContentsManager"

# Always pair ipynb notebooks to py files
c.ContentsManager.default_jupytext_formats = "ipynb,py"' >> $HOME/.jupyter/jupyter_notebook_config.py
