import webui
import app as user_src

user_src.init()

if __name__ == '__main__':
    global model
    import modules.sd_models
    modules.script_callbacks.before_ui_callback()
    webui.api_only()