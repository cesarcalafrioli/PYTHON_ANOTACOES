# Example - 1
numbers = [run_calculation(i) for i in range(10)]

# Example - 2
def collect_accounts_ids_from_arns(arns):
    matched_arns = filter(None, (re.match(ARN_REGEX, arn) for ar))
    return {m.groupdict()["account_id"] for m in matched_arns}

# Example 3 - PEP 572 - After Python 3.8
def collection_account_ids_from_arns(arns: Iterable[str]) -> Set[str]:
    return {
        matched.groupdict()["account_it"]
        for arn in arns
        if ( matched := re.match(ARN_REGEX, arn)) is not None
    }