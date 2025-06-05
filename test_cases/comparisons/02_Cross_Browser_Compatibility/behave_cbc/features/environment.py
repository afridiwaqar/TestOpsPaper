import time

def after_scenario(context, scenario):
    if hasattr(context, 'browser'):
        context.end_time = time.time()
        elapsed_time = context.end_time - context.start_time
        print(f"{context.browser.name} scenario '{scenario.name}' took {elapsed_time:.2f} seconds.")

