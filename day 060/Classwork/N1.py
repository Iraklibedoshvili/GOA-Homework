class account:
    count=0
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        account.count +=1
        def get_owner(self):
            return self._owner
        def get_balance(self):
            return self._balance
        @classmethod
        def get_object_count(cls):
            return cls._object_count