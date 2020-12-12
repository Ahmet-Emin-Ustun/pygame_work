import pygame
import pygame_gui

from pygame_gui.elements import UIWindow
from pygame_gui.elements import UIButton
from pygame_gui.elements import UISelectionList

class Window(UIWindow):
  def __init__(self, Rect, manager,menuData,llr,x):
        super().__init__(Rect,
                         manager,
                         'ayarlar',
                         element_id='GUI_Window',
                         object_id='#gui_window',
                         resizable=True)
        self.manager = manager
        self.llr = llr
        self.menuData = menuData        
        self.x = x   
        if x == False:
         self.slider = pygame_gui.elements.UIScrollingContainer(pygame.Rect((0,0), (200, 500)),
                                                               starting_height=200,
                                                               manager =manager,
                                                               container=self,
                                                               object_id="#qqq",
                                                                anchors={
                                                                 'left': 'left',
                                                                 'right': 'left',
                                                                 'top': 'top',
                                                                 'bottom': 'top'
                                                                              })
         self.buton1 = pygame_gui.elements.UIButton(pygame.Rect((65,130), (50, 50)),
                               'Tuş 1',
                               manager,
                               container=self.slider,
                               tool_tip_text='Sesi arttır',
                               object_id='#xya',
                               anchors={
                                   'left': 'left',
                                   'right': 'left',
                                   'top': 'top',
                                   'bottom': 'top'
                               }) 
         self.buton2 = pygame_gui.elements.UIButton(pygame.Rect((15,130), (50, 50)),
                               'Tuş 2',
                               manager,
                               container=self.slider,
                               tool_tip_text='Sesi kıs',
                               object_id='#xyY',
                               anchors={
                                   'left': 'left',
                                   'right': 'left',
                                   'top': 'top',
                                   'bottom': 'top'
                               })
         self.txext = pygame_gui.elements.UITextEntryLine(pygame.Rect((15,100),(120,100)),
                                                        manager,
                                                        container=self.slider,
                                                        object_id='#himm',
                                                        anchors={
                                                                 'left': 'left',
                                                                 'right': 'left',
                                                                 'top': 'top',
                                                                 'bottom': 'top'
                                                                              })  
         self.lisansira = pygame_gui.elements.ui_selection_list.UISelectionList(pygame.Rect((15,55),(100,25)),
                                                                menuData,
                                                                 manager,
                                                                 container=self.slider,
                                                                 allow_double_clicks=True,
                                                                 starting_height=10,
                                                                 object_id='#gkaujoa',
                                                               anchors={
                                                                 'left': 'left',
                                                                 'right': 'left',
                                                                 'top': 'top',
                                                                 'bottom': 'top'
                                                                              } )
         self.box = pygame_gui.elements.UITextBox(llr,
                                                pygame.Rect((15,15),(150,35)),
                                                manager,
                                                layer_starting_height=100,
                                                container=self.slider,
                                                object_id='#gkaoa',
                                                anchors={
                                                'left': 'left',
                                                'right': 'left',
                                                'top': 'top',
                                                'bottom': 'top'
                                                    })   
        else:
            self.kutu = pygame_gui.elements.UITextBox("GİRİŞ BAŞARILI",
                                                       pygame.Rect((15,15),(400,300)),
                                                       manager,
                                                       layer_starting_height=100,
                                                       container=self,
                                                        object_id='#gkaoa',
                                                       anchors={
                                                        'left': 'left',
                                                        'right': 'left',
                                                        'top': 'top',
                                                         'bottom': 'top'
                                                        })                                                                    

tmk = {'#secin_butonu' : {
    'display_name' : 'Seçin:',
    'items' : {
        '#secim1': {
            'display_name': 'seçim 1'},
        '#secim2': {
            'display_name': 'seçim 2'}}}
            }

pygame.init()
pygame.display.set_caption('Quick Start')

e = False
q = False

window_surface = pygame.display.set_mode((800, 600))
  
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#004D40'))

manager = pygame_gui.UIManager((800, 600),'tema.json')

  
buton = pygame_gui.elements.UIButton(pygame.Rect((150, 150), (50, 50)),
                               'Hello!',
                               manager,
                               tool_tip_text='"Hello!" yazdıran bi button',
                               object_id='#merhaba_butonu_1',
                              anchors={
                                   'left': 'left',
                                   'right': 'right',
                                   'top': 'top',
                                   'bottom': 'bottom'
                               })
   
is_running = True
clock = pygame.time.Clock()
qr = "seçin"

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == buton:
                    e=False
                    pen = Window(pygame.Rect((0,0), (500, 500)),manager,tmk,qr,e)
                if event.ui_element == pen.buton1:
                    print("Tuş 1 tetklendi")
                if event.ui_element == pen.buton2:
                    print("Tuş 2 tetiklendi")
            elif event.user_type == pygame_gui.UI_WINDOW_CLOSE:
                if event.ui_object_id == '#gui_window':
                    pen.activeCanvas = event.ui_element
            elif event.user_type == pygame_gui.UI_SELECTION_LIST_DOUBLE_CLICKED_SELECTION:
                if event.ui_element == pen.lisansira:
                    print("2 kere tıklandı")
                    pen.lisansira.rebuild()
            elif event.user_type == pygame_gui.UI_SELECTION_LIST_DROPPED_SELECTION:
                if event.ui_element == pen.lisansira:
                    print("listelendi")
                    pen.lisansira.rebuild()
            elif event.user_type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                if event.ui_element == pen.lisansira:
                    print("Seçilen:", event.text)
            elif event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                lg = pen.txext.get_text() 
                if lg == "bruh":
                    q = True
                    p2n =  Window(pygame.Rect((0,0), (500, 500)),manager,tmk,qr,q)
                else:
                    print("hata")
                 

        window_surface.blit(background,(0, 0))

        manager.process_events(event)

        manager.update(time_delta)
   
        manager.draw_ui(window_surface)

        pygame.display.update()