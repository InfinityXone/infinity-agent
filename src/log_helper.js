import { createClient } from '@supabase/supabase-js';
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_SERVICE_KEY);

export async function logEvent(source, level, message, data = {}) {
  await supabase.from('system_logs').insert([
    { source, level, message, data }
  ]);
}

// Example usage
// await logEvent('GPT', 'INFO', 'Prompt generated', { promptText });
// await logEvent('Infinity Agent', 'ERROR', 'Browser crashed', { sessionId });
