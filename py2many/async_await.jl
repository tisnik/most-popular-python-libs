#[async]
function task()
println(join(["task started"], " "));
await!(sleep(asyncio, 5));
println(join(["task finished"], " "));
end

function main()
task1 = create_task(asyncio, task())
println(join(["task created"], " "));
await!(task1);
println(join(["done"], " "));
end

