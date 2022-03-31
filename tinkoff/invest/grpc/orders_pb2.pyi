"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import tinkoff.invest.grpc.common_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _OrderDirection:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _OrderDirectionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OrderDirection.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ORDER_DIRECTION_UNSPECIFIED: _OrderDirection.ValueType  # 0
    """Значение не указано"""

    ORDER_DIRECTION_BUY: _OrderDirection.ValueType  # 1
    """Покупка"""

    ORDER_DIRECTION_SELL: _OrderDirection.ValueType  # 2
    """Продажа"""

class OrderDirection(_OrderDirection, metaclass=_OrderDirectionEnumTypeWrapper):
    """Направление операции"""
    pass

ORDER_DIRECTION_UNSPECIFIED: OrderDirection.ValueType  # 0
"""Значение не указано"""

ORDER_DIRECTION_BUY: OrderDirection.ValueType  # 1
"""Покупка"""

ORDER_DIRECTION_SELL: OrderDirection.ValueType  # 2
"""Продажа"""

global___OrderDirection = OrderDirection


class _OrderType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _OrderTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OrderType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ORDER_TYPE_UNSPECIFIED: _OrderType.ValueType  # 0
    """Значение не указано"""

    ORDER_TYPE_LIMIT: _OrderType.ValueType  # 1
    """Лимитная"""

    ORDER_TYPE_MARKET: _OrderType.ValueType  # 2
    """Рыночная"""

class OrderType(_OrderType, metaclass=_OrderTypeEnumTypeWrapper):
    """Тип заявки"""
    pass

ORDER_TYPE_UNSPECIFIED: OrderType.ValueType  # 0
"""Значение не указано"""

ORDER_TYPE_LIMIT: OrderType.ValueType  # 1
"""Лимитная"""

ORDER_TYPE_MARKET: OrderType.ValueType  # 2
"""Рыночная"""

global___OrderType = OrderType


class _OrderExecutionReportStatus:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _OrderExecutionReportStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OrderExecutionReportStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    EXECUTION_REPORT_STATUS_UNSPECIFIED: _OrderExecutionReportStatus.ValueType  # 0
    EXECUTION_REPORT_STATUS_FILL: _OrderExecutionReportStatus.ValueType  # 1
    """Исполнена"""

    EXECUTION_REPORT_STATUS_REJECTED: _OrderExecutionReportStatus.ValueType  # 2
    """Отклонена"""

    EXECUTION_REPORT_STATUS_CANCELLED: _OrderExecutionReportStatus.ValueType  # 3
    """Отменена пользователем"""

    EXECUTION_REPORT_STATUS_NEW: _OrderExecutionReportStatus.ValueType  # 4
    """Новая"""

    EXECUTION_REPORT_STATUS_PARTIALLYFILL: _OrderExecutionReportStatus.ValueType  # 5
    """Частично исполнена"""

class OrderExecutionReportStatus(_OrderExecutionReportStatus, metaclass=_OrderExecutionReportStatusEnumTypeWrapper):
    """Текущий статус заявки (поручения)"""
    pass

EXECUTION_REPORT_STATUS_UNSPECIFIED: OrderExecutionReportStatus.ValueType  # 0
EXECUTION_REPORT_STATUS_FILL: OrderExecutionReportStatus.ValueType  # 1
"""Исполнена"""

EXECUTION_REPORT_STATUS_REJECTED: OrderExecutionReportStatus.ValueType  # 2
"""Отклонена"""

EXECUTION_REPORT_STATUS_CANCELLED: OrderExecutionReportStatus.ValueType  # 3
"""Отменена пользователем"""

EXECUTION_REPORT_STATUS_NEW: OrderExecutionReportStatus.ValueType  # 4
"""Новая"""

EXECUTION_REPORT_STATUS_PARTIALLYFILL: OrderExecutionReportStatus.ValueType  # 5
"""Частично исполнена"""

global___OrderExecutionReportStatus = OrderExecutionReportStatus


class TradesStreamRequest(google.protobuf.message.Message):
    """Запрос установки соединения."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___TradesStreamRequest = TradesStreamRequest

class TradesStreamResponse(google.protobuf.message.Message):
    """Информация о торговых поручениях."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORDER_TRADES_FIELD_NUMBER: builtins.int
    PING_FIELD_NUMBER: builtins.int
    @property
    def order_trades(self) -> global___OrderTrades:
        """Информация об исполнении торгового поручения."""
        pass
    @property
    def ping(self) -> tinkoff.invest.grpc.common_pb2.Ping:
        """Проверка активности стрима."""
        pass
    def __init__(self,
        *,
        order_trades: typing.Optional[global___OrderTrades] = ...,
        ping: typing.Optional[tinkoff.invest.grpc.common_pb2.Ping] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["order_trades",b"order_trades","payload",b"payload","ping",b"ping"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["order_trades",b"order_trades","payload",b"payload","ping",b"ping"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["payload",b"payload"]) -> typing.Optional[typing_extensions.Literal["order_trades","ping"]]: ...
global___TradesStreamResponse = TradesStreamResponse

class OrderTrades(google.protobuf.message.Message):
    """Информация об исполнении торгового поручения."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORDER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    DIRECTION_FIELD_NUMBER: builtins.int
    FIGI_FIELD_NUMBER: builtins.int
    TRADES_FIELD_NUMBER: builtins.int
    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    order_id: typing.Text
    """Идентификатор торгового поручения"""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Дата и время создания сообщения в часовом поясе UTC."""
        pass
    direction: global___OrderDirection.ValueType
    """Направление сделки (возможные значения)"""

    figi: typing.Text
    """Figi-идентификатор инструмента"""

    @property
    def trades(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___OrderTrade]:
        """Массив сделок"""
        pass
    account_id: typing.Text
    """Идентификатор счёта"""

    def __init__(self,
        *,
        order_id: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        direction: global___OrderDirection.ValueType = ...,
        figi: typing.Text = ...,
        trades: typing.Optional[typing.Iterable[global___OrderTrade]] = ...,
        account_id: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_id",b"account_id","created_at",b"created_at","direction",b"direction","figi",b"figi","order_id",b"order_id","trades",b"trades"]) -> None: ...
global___OrderTrades = OrderTrades

class OrderTrade(google.protobuf.message.Message):
    """Информация о сделке."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATE_TIME_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    QUANTITY_FIELD_NUMBER: builtins.int
    @property
    def date_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Дата и время совершения сделки в часовом поясе UTC."""
        pass
    @property
    def price(self) -> tinkoff.invest.grpc.common_pb2.Quotation:
        """Цена, по которой совершена сделка"""
        pass
    quantity: builtins.int
    """Количество лотов в сделке"""

    def __init__(self,
        *,
        date_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        price: typing.Optional[tinkoff.invest.grpc.common_pb2.Quotation] = ...,
        quantity: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["date_time",b"date_time","price",b"price"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["date_time",b"date_time","price",b"price","quantity",b"quantity"]) -> None: ...
global___OrderTrade = OrderTrade

class PostOrderRequest(google.protobuf.message.Message):
    """Запрос выставления торгового поручения."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FIGI_FIELD_NUMBER: builtins.int
    QUANTITY_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    DIRECTION_FIELD_NUMBER: builtins.int
    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    ORDER_TYPE_FIELD_NUMBER: builtins.int
    ORDER_ID_FIELD_NUMBER: builtins.int
    figi: typing.Text
    """Figi-идентификатор инструмента."""

    quantity: builtins.int
    """Количество лотов."""

    @property
    def price(self) -> tinkoff.invest.grpc.common_pb2.Quotation:
        """Цена лота."""
        pass
    direction: global___OrderDirection.ValueType
    """Направление операции."""

    account_id: typing.Text
    """Номер счёта."""

    order_type: global___OrderType.ValueType
    """Тип заявки."""

    order_id: typing.Text
    """Идентификатор запроса выставления поручения для целей идемпотентности. Максимальная длина 36 символов."""

    def __init__(self,
        *,
        figi: typing.Text = ...,
        quantity: builtins.int = ...,
        price: typing.Optional[tinkoff.invest.grpc.common_pb2.Quotation] = ...,
        direction: global___OrderDirection.ValueType = ...,
        account_id: typing.Text = ...,
        order_type: global___OrderType.ValueType = ...,
        order_id: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["price",b"price"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_id",b"account_id","direction",b"direction","figi",b"figi","order_id",b"order_id","order_type",b"order_type","price",b"price","quantity",b"quantity"]) -> None: ...
global___PostOrderRequest = PostOrderRequest

class PostOrderResponse(google.protobuf.message.Message):
    """Информация о выставлении поручения."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORDER_ID_FIELD_NUMBER: builtins.int
    EXECUTION_REPORT_STATUS_FIELD_NUMBER: builtins.int
    LOTS_REQUESTED_FIELD_NUMBER: builtins.int
    LOTS_EXECUTED_FIELD_NUMBER: builtins.int
    INITIAL_ORDER_PRICE_FIELD_NUMBER: builtins.int
    EXECUTED_ORDER_PRICE_FIELD_NUMBER: builtins.int
    TOTAL_ORDER_AMOUNT_FIELD_NUMBER: builtins.int
    INITIAL_COMMISSION_FIELD_NUMBER: builtins.int
    EXECUTED_COMMISSION_FIELD_NUMBER: builtins.int
    ACI_VALUE_FIELD_NUMBER: builtins.int
    FIGI_FIELD_NUMBER: builtins.int
    DIRECTION_FIELD_NUMBER: builtins.int
    INITIAL_SECURITY_PRICE_FIELD_NUMBER: builtins.int
    ORDER_TYPE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    INITIAL_ORDER_PRICE_PT_FIELD_NUMBER: builtins.int
    order_id: typing.Text
    """Идентификатор заявки."""

    execution_report_status: global___OrderExecutionReportStatus.ValueType
    """Текущий статус заявки."""

    lots_requested: builtins.int
    """Запрошено лотов."""

    lots_executed: builtins.int
    """Исполнено лотов."""

    @property
    def initial_order_price(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Начальная цена заявки. Произведение количества запрошенных лотов на цену."""
        pass
    @property
    def executed_order_price(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Исполненная цена заявки. Произведение средней цены покупки на количество лотов."""
        pass
    @property
    def total_order_amount(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Итоговая стоимость заявки, включающая все комиссии."""
        pass
    @property
    def initial_commission(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Начальная комиссия. Комиссия рассчитанная при выставлении заявки."""
        pass
    @property
    def executed_commission(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Фактическая комиссия по итогам исполнения заявки."""
        pass
    @property
    def aci_value(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Значение НКД (накопленного купонного дохода) на дату. Подробнее: [НКД при выставлении торговых поручений](https://tinkoff.github.io/investAPI/head-orders#coupon)"""
        pass
    figi: typing.Text
    """Figi-идентификатор инструмента."""

    direction: global___OrderDirection.ValueType
    """Направление сделки."""

    @property
    def initial_security_price(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Начальная цена инструмента заявки."""
        pass
    order_type: global___OrderType.ValueType
    """Тип заявки."""

    message: typing.Text
    """Дополнительные данные об исполнении заявки."""

    @property
    def initial_order_price_pt(self) -> tinkoff.invest.grpc.common_pb2.Quotation:
        """Начальная цена заявки в пунктах (для фьючерсов)."""
        pass
    def __init__(self,
        *,
        order_id: typing.Text = ...,
        execution_report_status: global___OrderExecutionReportStatus.ValueType = ...,
        lots_requested: builtins.int = ...,
        lots_executed: builtins.int = ...,
        initial_order_price: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        executed_order_price: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        total_order_amount: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        initial_commission: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        executed_commission: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        aci_value: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        figi: typing.Text = ...,
        direction: global___OrderDirection.ValueType = ...,
        initial_security_price: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        order_type: global___OrderType.ValueType = ...,
        message: typing.Text = ...,
        initial_order_price_pt: typing.Optional[tinkoff.invest.grpc.common_pb2.Quotation] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["aci_value",b"aci_value","executed_commission",b"executed_commission","executed_order_price",b"executed_order_price","initial_commission",b"initial_commission","initial_order_price",b"initial_order_price","initial_order_price_pt",b"initial_order_price_pt","initial_security_price",b"initial_security_price","total_order_amount",b"total_order_amount"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["aci_value",b"aci_value","direction",b"direction","executed_commission",b"executed_commission","executed_order_price",b"executed_order_price","execution_report_status",b"execution_report_status","figi",b"figi","initial_commission",b"initial_commission","initial_order_price",b"initial_order_price","initial_order_price_pt",b"initial_order_price_pt","initial_security_price",b"initial_security_price","lots_executed",b"lots_executed","lots_requested",b"lots_requested","message",b"message","order_id",b"order_id","order_type",b"order_type","total_order_amount",b"total_order_amount"]) -> None: ...
global___PostOrderResponse = PostOrderResponse

class CancelOrderRequest(google.protobuf.message.Message):
    """Запрос отмены торгового поручения."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    ORDER_ID_FIELD_NUMBER: builtins.int
    account_id: typing.Text
    """Номер счёта."""

    order_id: typing.Text
    """Идентификатор заявки."""

    def __init__(self,
        *,
        account_id: typing.Text = ...,
        order_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_id",b"account_id","order_id",b"order_id"]) -> None: ...
global___CancelOrderRequest = CancelOrderRequest

class CancelOrderResponse(google.protobuf.message.Message):
    """Результат отмены торгового поручения."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TIME_FIELD_NUMBER: builtins.int
    @property
    def time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Дата и время отмены заявки в часовом поясе UTC."""
        pass
    def __init__(self,
        *,
        time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["time",b"time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["time",b"time"]) -> None: ...
global___CancelOrderResponse = CancelOrderResponse

class GetOrderStateRequest(google.protobuf.message.Message):
    """Запрос получения статуса торгового поручения."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    ORDER_ID_FIELD_NUMBER: builtins.int
    account_id: typing.Text
    """Номер счёта."""

    order_id: typing.Text
    """Идентификатор заявки."""

    def __init__(self,
        *,
        account_id: typing.Text = ...,
        order_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_id",b"account_id","order_id",b"order_id"]) -> None: ...
global___GetOrderStateRequest = GetOrderStateRequest

class GetOrdersRequest(google.protobuf.message.Message):
    """Запрос получения списка активных торговых поручений."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    account_id: typing.Text
    """Номер счёта."""

    def __init__(self,
        *,
        account_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_id",b"account_id"]) -> None: ...
global___GetOrdersRequest = GetOrdersRequest

class GetOrdersResponse(google.protobuf.message.Message):
    """Список активных торговых поручений."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORDERS_FIELD_NUMBER: builtins.int
    @property
    def orders(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___OrderState]:
        """Массив активных заявок."""
        pass
    def __init__(self,
        *,
        orders: typing.Optional[typing.Iterable[global___OrderState]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["orders",b"orders"]) -> None: ...
global___GetOrdersResponse = GetOrdersResponse

class OrderState(google.protobuf.message.Message):
    """Информация о торговом поручении."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORDER_ID_FIELD_NUMBER: builtins.int
    EXECUTION_REPORT_STATUS_FIELD_NUMBER: builtins.int
    LOTS_REQUESTED_FIELD_NUMBER: builtins.int
    LOTS_EXECUTED_FIELD_NUMBER: builtins.int
    INITIAL_ORDER_PRICE_FIELD_NUMBER: builtins.int
    EXECUTED_ORDER_PRICE_FIELD_NUMBER: builtins.int
    TOTAL_ORDER_AMOUNT_FIELD_NUMBER: builtins.int
    AVERAGE_POSITION_PRICE_FIELD_NUMBER: builtins.int
    INITIAL_COMMISSION_FIELD_NUMBER: builtins.int
    EXECUTED_COMMISSION_FIELD_NUMBER: builtins.int
    FIGI_FIELD_NUMBER: builtins.int
    DIRECTION_FIELD_NUMBER: builtins.int
    INITIAL_SECURITY_PRICE_FIELD_NUMBER: builtins.int
    STAGES_FIELD_NUMBER: builtins.int
    SERVICE_COMMISSION_FIELD_NUMBER: builtins.int
    CURRENCY_FIELD_NUMBER: builtins.int
    ORDER_TYPE_FIELD_NUMBER: builtins.int
    ORDER_DATE_FIELD_NUMBER: builtins.int
    order_id: typing.Text
    """Идентификатор заявки."""

    execution_report_status: global___OrderExecutionReportStatus.ValueType
    """Текущий статус заявки."""

    lots_requested: builtins.int
    """Запрошено лотов."""

    lots_executed: builtins.int
    """Исполнено лотов."""

    @property
    def initial_order_price(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Начальная цена заявки. Произведение количества запрошенных лотов на цену."""
        pass
    @property
    def executed_order_price(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Исполненная цена заявки. Произведение средней цены покупки на количество лотов."""
        pass
    @property
    def total_order_amount(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Итоговая стоимость заявки, включающая все комиссии."""
        pass
    @property
    def average_position_price(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Средняя цена позиции по сделке."""
        pass
    @property
    def initial_commission(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Начальная комиссия. Комиссия, рассчитанная на момент подачи заявки."""
        pass
    @property
    def executed_commission(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Фактическая комиссия по итогам исполнения заявки."""
        pass
    figi: typing.Text
    """Figi-идентификатор инструмента."""

    direction: global___OrderDirection.ValueType
    """Направление заявки."""

    @property
    def initial_security_price(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Начальная цена инструмента. Цена инструмента на момент выставления заявки."""
        pass
    @property
    def stages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___OrderStage]:
        """Стадии выполнения заявки."""
        pass
    @property
    def service_commission(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Сервисная комиссия."""
        pass
    currency: typing.Text
    """Валюта заявки."""

    order_type: global___OrderType.ValueType
    """Тип заявки."""

    @property
    def order_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Дата и время выставления заявки в часовом поясе UTC."""
        pass
    def __init__(self,
        *,
        order_id: typing.Text = ...,
        execution_report_status: global___OrderExecutionReportStatus.ValueType = ...,
        lots_requested: builtins.int = ...,
        lots_executed: builtins.int = ...,
        initial_order_price: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        executed_order_price: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        total_order_amount: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        average_position_price: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        initial_commission: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        executed_commission: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        figi: typing.Text = ...,
        direction: global___OrderDirection.ValueType = ...,
        initial_security_price: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        stages: typing.Optional[typing.Iterable[global___OrderStage]] = ...,
        service_commission: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        currency: typing.Text = ...,
        order_type: global___OrderType.ValueType = ...,
        order_date: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["average_position_price",b"average_position_price","executed_commission",b"executed_commission","executed_order_price",b"executed_order_price","initial_commission",b"initial_commission","initial_order_price",b"initial_order_price","initial_security_price",b"initial_security_price","order_date",b"order_date","service_commission",b"service_commission","total_order_amount",b"total_order_amount"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["average_position_price",b"average_position_price","currency",b"currency","direction",b"direction","executed_commission",b"executed_commission","executed_order_price",b"executed_order_price","execution_report_status",b"execution_report_status","figi",b"figi","initial_commission",b"initial_commission","initial_order_price",b"initial_order_price","initial_security_price",b"initial_security_price","lots_executed",b"lots_executed","lots_requested",b"lots_requested","order_date",b"order_date","order_id",b"order_id","order_type",b"order_type","service_commission",b"service_commission","stages",b"stages","total_order_amount",b"total_order_amount"]) -> None: ...
global___OrderState = OrderState

class OrderStage(google.protobuf.message.Message):
    """Сделки в рамках торгового поручения."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PRICE_FIELD_NUMBER: builtins.int
    QUANTITY_FIELD_NUMBER: builtins.int
    TRADE_ID_FIELD_NUMBER: builtins.int
    @property
    def price(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Цена."""
        pass
    quantity: builtins.int
    """Количество лотов."""

    trade_id: typing.Text
    """Идентификатор торговой операции."""

    def __init__(self,
        *,
        price: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        quantity: builtins.int = ...,
        trade_id: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["price",b"price"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["price",b"price","quantity",b"quantity","trade_id",b"trade_id"]) -> None: ...
global___OrderStage = OrderStage
