import random
import uuid
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
    prediction_status: str
    cluster_id: str
    upgrade_risks_predictors: list[UpgradeRisksPredictors]


def generate_alerts():
    names = ["CriticalAlert", "SecurityAlert", "InfoAlert"]
    namespaces = ["openshift-kube-apiserver"]
    severities = ["info", "warning", "error", "critical"]
    alerts = []
    for i in range(random.randrange(1, 5)):
        alert = Alert(
            name=random.choice(names),
            namespace=random.choice(namespaces),
            severity=random.choice(severities),
        )
        alerts.append(alert)
    return alerts


def generate_operator_conditions():
    conds = []
    names = ["authentication", "security", "networking", "performance"]
    conditions = ["Degraded", "Untrusted", "Security check"]
    for i in range(random.randrange(1, 5)):
        cond = OperatorCondition(
            name=random.choice(names),
            condition=random.choice(conditions),
            reason="AsExpected",
        )
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
    upgrade_risks_predictors = []
    if not recommended:
        upgrade_risks_predictors = retrieve_predictions()

    return UpgradePrediction(
        cluster_id=uuid.uuid4(),
        recommended=recommended,
        last_checked_at=datetime.now(),
        upgrade_risks_predictors=upgrade_risks_predictors,
        prediction_status="ok",
    )


@strawberry.type
class Query:
    upgrade_prediction: UpgradePrediction = strawberry.field(
        resolver=upgrade_prediction
    )


schema = strawberry.Schema(query=Query)
