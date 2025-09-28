import { createClient } from '@supabase/supabase-js';
import fetch from 'node-fetch';

const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_SERVICE_KEY);

// Save GPT messages to persistent memory
export async function saveGPTMessage(conversationId, role, content) {
  await supabase.from('gpt_memory').insert([
    { conversation_id: conversationId, message_role: role, content }
  ]);
}

// Fetch recent context for GPT
export async function fetchGPTContext(conversationId, limit = 10) {
  const { data } = await supabase
    .from('gpt_memory')
    .select('message_role, content')
    .eq('conversation_id', conversationId)
    .order('created_at', { ascending: false })
    .limit(limit);

  return data.reverse(); // Oldest → Newest
}
