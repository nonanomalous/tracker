class GetterMixin:
    ###############
    ### STATUS
    ###############

    @classmethod
    def NewId(cls):
        obj = cls.objects.filter(name="New").first()
        return obj.id if obj else 1

    @classmethod
    def New(cls):
        return cls.objects.filter(name="New").first()
    
    @classmethod
    def ResolvedId(cls):
        obj = cls.objects.filter(name="Resolved").first()
        return obj.id if obj else 1
    
    @classmethod
    def Resolved(cls):
        return cls.objects.filter(name="Resolved").first()
    
    @classmethod
    def ClosedId(cls):
        obj = cls.objects.filter(name="Closed").first()
        return obj.id if obj else 1
    
    @classmethod
    def EscalatedId(cls):
        obj = cls.objects.filter(name="Escalated").first()
        return obj.id if obj else 1
    
    @classmethod
    def Closed(cls):
        return cls.objects.filter(name="Closed").first()

    ###############
    ### SUBCATEGORY 
    ###############

    @classmethod
    def GeneralId(cls):
        obj = cls.objects.filter(name="General").first()
        return obj.id if obj else 1

    ###############
    ### REASON
    ###############
    
    @classmethod
    def CreatedId(cls):
        obj = cls.objects.filter(name="Created").first()
        return obj.id if obj else 1
    
    ###############
    ### GROUP
    ###############
    
    @classmethod
    def Level1Id(cls):
        obj = cls.objects.filter(name="Level1").first()
        return obj.id if obj else 1
    
    @classmethod
    def Level1(cls):
        return cls.objects.filter(name="Level1").first()
    
    @classmethod
    def Level2Id(cls):
        obj = cls.objects.filter(name="Level2").first()
        return obj.id if obj else 1
    
    @classmethod
    def Level2(cls):
        return cls.objects.filter(name="Level2").first()
    
    @classmethod
    def Level3Id(cls):
        obj = cls.objects.filter(name="Level3").first()
        return obj.id if obj else 1
    
    @classmethod
    def Level3(cls):
        return cls.objects.filter(name="Level3").first()
    
