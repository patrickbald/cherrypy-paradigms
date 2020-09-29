#!/escnfs/home/csesoft/2017-fall/anaconda3/bin/python3

import cherrypy
import routes
from dictionary_controller import DictionaryController # getting our controller class 

def start_service():
    '''configures and runs the server'''
    dCon = DictionaryController() # object

    dispatcher = cherrypy.dispatch.RoutesDispatcher() # dispatcher object
    # we will use this to connect endpoints to controllers

    # connecting endpoints to resources
    #connect(out_tag, http resource, class object with handler, event handler name, what type of HTTP request to serve)
    dispatcher.connect('dict_get_key', '/dictionary/:key', controller=dCon, action='GET_KEY', conditions=dict(method=['GET']))
    dispatcher.connect('dict_put_key', '/dictionary/:key', controller=dCon, action='PUT_KEY', conditions=dict(method=['PUT']))

    
    # configuration for the server
    conf = {
            'global' : {
                'server.socket_host' : 'student10.cse.nd.edu', # can use 'localhost' instead, then remember to test with localhost
                'server.socket_port' : 51075, 
                },
            '/' : {
                'request.dispatch' : dispatcher, # our dispatcher object
                }
            }
    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf) # creates the app
    cherrypy.quickstart(app)


if __name__ == '__main__':
    start_service()

