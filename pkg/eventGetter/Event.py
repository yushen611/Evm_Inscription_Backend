import json


def dict_to_event(event_dict):
    event = Event()
    if 'address' in event_dict:
        event.address = event_dict['address']
    if 'topics' in event_dict:
        event.topics = event_dict['topics']
    if 'data' in event_dict:
        event.data = event_dict['data']
    if 'blockNumber' in event_dict:
        event.blockNumber = event_dict['blockNumber']
    if 'blockHash' in event_dict:
        event.blockHash = event_dict['blockHash']
    if 'timeStamp' in event_dict:
        event.timeStamp = event_dict['timeStamp']
    if 'gasPrice' in event_dict:
        event.gasPrice = event_dict['gasPrice']
    if 'gasUsed' in event_dict:
        event.gasUsed = event_dict['gasUsed']
    if 'logIndex' in event_dict:
        event.logIndex = event_dict['logIndex']
    if 'transactionHash' in event_dict:
        event.transactionHash = event_dict['transactionHash']
    if 'transactionIndex' in event_dict:
        event.transactionIndex = event_dict['transactionIndex']

    return event


class Event:
    def __init__(self):
        self._address = None
        self._topics = None
        self._data = None
        self._blockNumber = None
        self._blockHash = None
        self._timeStamp = None
        self._gasPrice = None
        self._gasUsed = None
        self._logIndex = None
        self._transactionHash = None
        self._transactionIndex = None
        self._sender = None

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, value):
        self._sender = value


    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def topics(self):
        return self._topics

    @topics.setter
    def topics(self, value):
        self._topics = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def blockNumber(self):
        return self._blockNumber

    @blockNumber.setter
    def blockNumber(self, value):
        self._blockNumber = value

    @property
    def blockHash(self):
        return self._blockHash

    @blockHash.setter
    def blockHash(self, value):
        self._blockHash = value

    @property
    def timeStamp(self):
        return self._timeStamp

    @timeStamp.setter
    def timeStamp(self, value):
        self._timeStamp = value

    @property
    def gasPrice(self):
        return self._gasPrice

    @gasPrice.setter
    def gasPrice(self, value):
        self._gasPrice = value

    @property
    def gasUsed(self):
        return self._gasUsed

    @gasUsed.setter
    def gasUsed(self, value):
        self._gasUsed = value

    @property
    def logIndex(self):
        return self._logIndex

    @logIndex.setter
    def logIndex(self, value):
        self._logIndex = value

    @property
    def transactionHash(self):
        return self._transactionHash

    @transactionHash.setter
    def transactionHash(self, value):
        self._transactionHash = value

    @property
    def transactionIndex(self):
        return self._transactionIndex

    @transactionIndex.setter
    def transactionIndex(self, value):
        self._transactionIndex = value

    def __str__(self):
        return f"Event(" \
               f"sender={self.sender}, " \
               f"contract_address={self.address}, " \
               f"topics={self.topics}, " \
               f"data={self.data}, " \
               f"blockNumber={self.blockNumber}, " \
               f"blockHash={self.blockHash}, " \
               f"timeStamp={self.timeStamp}, " \
               f"gasPrice={self.gasPrice}, " \
               f"gasUsed={self.gasUsed}, " \
               f"logIndex={self.logIndex}, " \
               f"transactionHash={self.transactionHash}, " \
               f"transactionIndex={self.transactionIndex})"


