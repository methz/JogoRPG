class Player():
    def __init__(self):
        self.name = input('Escolha o nome do seu personagem: ')
        print('Olá', self.name, '!\n Bem vindo ao Brasil 2049...')

        self.level = 1
        self.hp = 100
        jobsMessage = '''
        Clases disponíveis (escolha a letra correspondente em destaque):
            - Pro(g)ramador
            - (M)édico
            - (P)rofessor
        '''
        print(jobsMessage)
        self.job = input('Escolha a classe do personagem: ')
        while(self.job.lower() != 'g' and self.job.lower() != 'm' and self.job.lower() != 'p'):
            self.job = input('Opção Inválida. \n Informe a classe do personagem: ')
        
        if(self.job == 'g'):
            self.job = 'Programador'
            self.weapon = 'Garrafa de Café'
        elif (self.job == 'm'):
            self.job = 'Médico'
            self.weapon = 'Bisturi'
        else:
            self.job = 'Professor'
            self.weapon = 'Retroprojetor'
        print(self.job)