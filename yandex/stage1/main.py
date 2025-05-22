import random
from abc import ABC, abstractmethod
from collections import defaultdict

import pytest as pytest


@pytest.fixture
def atm():
    sdk = SDKImpl()
    return ATM(sdk=sdk)


@pytest.mark.parametrize('amount,is_valid', (
        (0, False),
        (1, False),
        (50, True),
        (101, False),
        (5000, True),
        (1_000_050, False),
))
def test_amount_is_valid(atm, amount, is_valid):
    if is_valid:
        atm.get_banknotes(amount)
    else:
        with pytest.raises(AssertionError):
            atm.get_banknotes(amount)


@pytest.mark.parametrize('amount', (
        (50, {50: 1}),
        (5150, {}),
        (1_000_050, False),
))
def test_get_banknotes__ok(atm, amount):
    # TODO: Начальные условия
    # TODO: Проверять разбивку на купюры
    # TODO: Проверять остатки
    # TODO: Проверять вызовы SDK

    # Подготовка

    # Действие
    counts = atm.get_banknotes(amount)

    # Проверка


def test_get_banknotes__not_enough_nominals(atm, amount):
    # TODO
    raise NotImplemented


class NotEnoughNominals(Exception):
    pass


# Банкомат.
# Инициализируется набором купюр и умеет выдавать купюры для заданной суммы, либо отвечать отказом.
# При выдаче купюры списываются с баланса банкомата.
# Допустимые номиналы: 50₽, 100₽, 500₽, 1000₽, 5000₽.
class ATM:
    NOMINALS = (5000, 1000, 500, 100, 50)

    def __init__(self, sdk: 'SDK'):
        self.sdk = sdk
        counts = defaultdict(int)
        for nominal in self.NOMINALS:
            counts[nominal] = sdk.count_banknotes(nominal)
        self.repo_counts = counts

    @staticmethod
    def _validate_amount(amount: int):
        assert 0 < amount < 1_000_001
        assert amount % 50 == 0, "Сумма должна быть кратна 50 р"

    def _get_required_counts(self, amount: int) -> dict[int, int]:
        rest = amount
        counts = defaultdict(int)
        for nominal in ATM.NOMINALS:
            count = rest // nominal
            counts[nominal] = min(self.repo_counts[nominal], count)
            rest = rest - counts[nominal] * nominal
        if rest > 0:
            raise NotEnoughNominals
        return counts

    def get_banknotes(self, amount: int) -> dict[int, int]:
        self._validate_amount(amount)
        required_counts = self._get_required_counts(amount)
        for nominal in ATM.NOMINALS:
            count = required_counts[nominal]
            if count > 0:
                self.sdk.move_banknote_to_dispenser(banknote=nominal, count=count)
                self.repo_counts[nominal] -= count
        self.sdk.open_dispenser()
        return required_counts


# API для взаимодействия с аппаратурой банкомата.
# Краткий ликбез по устройству банкомата:
# - деньги расположены в кассетах, кассеты устанавливаются инкассацией;
# - в каждой кассете лежат свои купюры, количество известно инкассатору при установке
# - банкомат может подсчитать оставшиеся в кассетах банкноты, но эта операция занимает около 10 секунд, и шумная, её стоит вызывать как можно реже.
# - интерфейс SDK может быть изменён/расширен по договорённости сторон, если это необходимо
class SDK(ABC):
    @abstractmethod
    def count_banknotes(self, banknote: int) -> int:
        # долго и шумно
        pass

    @abstractmethod
    def move_banknote_to_dispenser(self, banknote: int, count: int) -> None:
        pass

    @abstractmethod
    def open_dispenser(self) -> None:
        pass


class SDKImpl(SDK):
    def count_banknotes(self, banknote: int) -> int:
        # долго и шумно
        return random.randint(0, 20)

    def move_banknote_to_dispenser(self, banknote: int, count: int) -> None:
        pass

    def open_dispenser(self) -> None:
        pass
