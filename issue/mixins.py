class GetterMixin:
    ###############
    ### STATUS
    ###############

    @classmethod
    def NewId(cls):
        obj, _ = cls.objects.get_or_create(name="New")
        return obj.id
    
    @classmethod
    def ClosedId(cls):
        obj, _ = cls.objects.get_or_create(name="Closed")
        return obj.id

    ###############
    ### SUBCATEGORY 
    ###############

    @classmethod
    def GeneralId(cls):
        obj, _ = cls.objects.get_or_create(name="General")
        return obj.id

    ###############
    ### REASON
    ###############
    
    @classmethod
    def CreatedId(cls):
        obj, _ = cls.objects.get_or_create(name="Created")
        return obj.id
    
    ###############
    ### GROUP
    ###############
    
    @classmethod
    def Level1Id(cls):
        obj, _ = cls.objects.get_or_create(name="Level1")
        return obj.id
    
