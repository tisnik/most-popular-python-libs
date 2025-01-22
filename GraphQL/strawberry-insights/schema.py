import random
from datetime import datetime
import strawberry


@strawberry.type
class Alert:
    name: str
    namespace: str
    severity: str


@strawberry.type
class OperatorCondition:
    name: str
    condition: str
    reason: str


@strawberry.type
class UpgradeRisksPredictors:
    alerts: list[Alert] | None
    operator_conditions: list[OperatorCondition] | None


@strawberry.type
class UpgradePrediction:
    recommended: bool
    last_checked_at: str
    upgrade_risks_predictors: list[UpgradeRisksPredictors]


def generate_alerts():
    alerts = []
    for i in range(random.randrange(1, 5)):
        alert = Alert(name="alert1", namespace="namespace1", severity="High")
        alerts.append(alert)
    return alerts


def generate_operator_conditions():
    conds = []
    for i in range(random.randrange(1, 5)):
        cond = OperatorCondition(name="cond1", condition="condition1", reason="reason1")
        conds.append(cond)
    return conds


def retrieve_predictions() -> list[UpgradeRisksPredictors]:
    predictions = []
    for i in range(random.randrange(1, 5)):
        prediction = UpgradeRisksPredictors(
            alerts=generate_alerts(), operator_conditions=generate_operator_conditions()
        )
        predictions.append(prediction)
    return predictions


def upgrade_prediction() -> UpgradePrediction:
    recommended = random.choice([True, False])
    recommended = False
    if recommended:
        return UpgradePrediction(
            recommended=recommended,
            last_checked_at=datetime.now(),
            upgrade_risks_predictors=[],
        )
    else:
        predictions = retrieve_predictions()
        return UpgradePrediction(
            recommended=recommended,
            last_checked_at=datetime.now(),
            upgrade_risks_predictors=predictions,
        )


@strawberry.type
class Query:
    upgrade_prediction: UpgradePrediction = strawberry.field(
        resolver=upgrade_prediction
    )


schema = strawberry.Schema(query=Query)
